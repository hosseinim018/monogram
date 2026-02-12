# Webhook Handling

## Overview

Monogram receives Telegram updates via HTTPS webhooks. The logic that sets webhooks, validates incoming requests, and turns raw JSON into typed `Update` objects lives in `webhook.py`. This page describes how an incoming webhook request is identified, bound to the correct bot, and converted into a typed `Update` for your code.

---

## Components in `webhook.py`

- **WebhookList** (View): Lists bots and supports creating new bots (GET/POST). Not part of the update pipeline.
- **WebhookHandler** (View): Handles both:
  - **GET** with `?action=set` / `?action=delete`: webhook setup and removal for a given bot.
  - **POST**: the actual webhook endpoint Telegram calls for each update.

The POST handler is where incoming JSON is identified, mapped to a bot, and converted to an `Update`.

---

## URL Routing and Bot Identification

Telegram sends updates to a single URL that you configure per bot via `setWebhook`. In Monogram, that URL includes the **bot name** so one Django app can serve many bots.

Typical pattern:

- Route: e.g. `/webhook/<botname>/`
- Example: `https://yourdomain.com/webhook/SupportBot/`

So the **bot instance is identified by the path**: the `botname` URL segment is used to load the corresponding `BotManager` from the database. No need to infer the bot from the payload; the URL determines which bot received the update.

---

## Flow: From Request to Typed Update

### 1. Request arrives (POST)

- Telegram POSTs a JSON body to your webhook URL.
- The body is a single [Update](https://core.telegram.org/bots/api#update) object: `update_id` plus one of `message`, `edited_message`, `callback_query`, `inline_query`, etc.

### 2. Resolve the bot

- The view extracts `botname` from the URL (e.g. `request.resolver_match.kwargs['botname']`).
- It loads the bot with:
  ```python
  bot = get_object_or_404(BotManager, name=botname)
  ```
- If no bot exists with that name, Django returns 404. No update is processed.

### 3. Secret token verification

- If the bot has a `secret_token` set, the view checks the header:
  ```python
  def _verify_secret_token(self, request, bot):
      if not bot.secret_token:
          return True
      incoming_token = request.headers.get('X-Telegram-Bot-Api-Secret-Token', '')
      return incoming_token == bot.secret_token
  ```
- If verification fails, the view returns `403 Forbidden` and the payload is not processed.
- This prevents third parties from sending fake updates to your endpoint.

### 4. Parse JSON and build Update

- The body is parsed once:
  ```python
  update_data = json.loads(request.body)
  ```
- If JSON is invalid, the view returns `400 Bad Request`.
- The payload is then turned into a typed `Update` and the bot reference is passed so nested types (e.g. `Message`) can use the bot if needed:
  ```python
  update = Update(bot=bot, **update_data)
  ```
- `Update.__init__` (in `monoTypes/Update.py`) uses the keys present in `update_data` to determine which kind of update it is and builds the corresponding nested type:
  - `message` → `Message(bot=bot, **update_data['message'])`
  - `callback_query` → `CallbackQuery(bot=bot, **...)`, with nested `Message` if present
  - `inline_query` → `InlineQuery(**...)`
  - and so on for all supported update types.

So after this step you have one typed `Update` object (with exactly one of its optional attributes set) and a clear link to the correct `BotManager` instance.

### 5. Process the update

- The view calls:
  ```python
  self._process_update(bot, update)
  ```
- `_process_update` then delegates to your bot logic. It uses the bot’s `object` field, which stores the dotted path to your bot class (e.g. `Bots.bot.bot1`):
  ```python
  def _process_update(self, bot, update):
      if not bot.object:
          logger.error(f"No bot class defined for {bot.name}")
          return
      module_path, class_name = bot.object.rsplit('.', 1)
      module = __import__(module_path, fromlist=[class_name])
      BotClass = getattr(module, class_name)
      bot_instance = BotClass(bot, update)
      # e.g. bot_instance.handle_update()
  ```
- So the **incoming JSON is identified by URL (bot name), mapped to the correct Bot instance (BotManager), and converted into a typed Update** before your `BotClass` is instantiated and used.

---

## Summary Diagram

```
Telegram server
    │
    │  POST /webhook/<botname>/
    │  Body: { "update_id": 123, "message": { ... } }
    │  Header: X-Telegram-Bot-Api-Secret-Token (optional)
    ▼
WebhookHandler.post()
    │
    ├─► get_object_or_404(BotManager, name=botname)  → bot
    ├─► _verify_secret_token(request, bot)           → 403 if invalid
    ├─► update_data = json.loads(request.body)        → 400 if invalid
    ├─► update = Update(bot=bot, **update_data)       → typed Update
    └─► _process_update(bot, update)                  → load BotClass(bot, update), run your logic
```

---

## Important Details

- **One update per request**: Telegram sends one Update per POST. Your handler runs once per update.
- **Response**: The view returns `HTTP 200` after successfully processing. Returning anything else or raising can cause Telegram to retry; handle errors and log as needed inside `_process_update`.
- **Bot in Update**: `Update` is constructed with `bot=bot`, so nested types (like `Message`) can receive the bot reference for later API calls (e.g. replying via the same bot).
- **Extensibility**: To support a new update type (e.g. a new field in the Telegram API), add the corresponding branch and type in `monoTypes/Update.py` and export the new type if necessary. The rest of the webhook flow stays the same.

This is how the incoming JSON is identified, mapped to the correct Bot instance, and converted into a typed `Update` for your application logic.
