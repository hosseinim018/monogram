# Monogram — Home

## Overview

**Monogram** is a Django-based Telegram Bot library that uses **webhooks** to receive updates. It is designed for production Django applications that need to host one or many bots with a clean, type-safe API that mirrors the [official Telegram Bot API](https://core.telegram.org/bots/api).

Monogram provides:

- **Django integration**: Each bot is a `BotManager` model instance—stored in the database, manageable via Django admin or custom views, and scalable within the Django ecosystem.
- **Webhook-first**: No long polling; updates are delivered via HTTPS to your Django app, with optional secret-token verification.
- **Direct API access**: Every bot instance exposes the full Telegram API surface. Call `bot.sendMessage(...)`, `bot.getMe()`, `bot.setWebhook(...)` and all other methods directly on the model instance.
- **Typed data**: Incoming and outgoing payloads are mapped to Python types in `monoTypes/`, so you work with `Update`, `Message`, `User`, `Chat`, and others instead of raw dictionaries.

---

## The "Typography" Philosophy

Monogram follows a **Typography** approach: the library’s structure and naming are aligned with the official Telegram Bot API documentation.

- **Methods**: API methods in `methods.py` are named and parameterized like the [Telegram API methods](https://core.telegram.org/bots/api#available-methods) (e.g. `sendMessage`, `getMe`, `setWebhook`). Adding or updating a method means following the same pattern and the same docs.
- **Types**: Objects in `monoTypes/` correspond to [Telegram API types](https://core.telegram.org/bots/api#available-types) (e.g. `Message`, `User`, `Chat`, `Update`). Each type inherits from `BaseType` and can be extended to match new fields or types from the docs.
- **Consistency**: By mirroring the official API, Monogram stays predictable and easy to extend as Telegram evolves—you translate the docs into methods and types without inventing a separate abstraction layer.

This philosophy keeps the codebase understandable and maintainable and makes it straightforward to add new methods or types when the Telegram API changes.

---

## The "Miracle" of BotManager

The central design choice is that **every bot instance is a Django model that directly inherits from Telegram Methods**.

```python
# models.py
class BotManager(Methods, models.Model):
    """Telegram Bot model with direct API method access"""
    name = models.CharField(max_length=100, unique=True)
    token = models.CharField(max_length=100)
    secret_token = models.CharField(max_length=100, blank=True, null=True)
    endpoint = models.CharField(max_length=100, default='api.telegram.org')
    # ... other fields
```

`BotManager` multiplies inheritance: it is both a **Django model** (persisted, queryable, configurable) and a **Methods** client (Telegram API). As a result:

1. **One object, two roles**: The same instance is the bot configuration in the DB and the object you use to call the API.
2. **No separate client**: You do not instantiate a separate "Telegram client" with the token; the model *is* the client. Load a bot with `BotManager.objects.get(name='MyBot')` and call `bot.sendMessage(chat_id=..., text='Hello')` on it.
3. **Credentials stay in sync**: Token, endpoint, proxy, and secret token are model fields. When you change and save the model, the underlying Methods/Network layer is reinitialized with the new credentials, so the object always reflects the stored configuration.

This "miracle" is what allows idiomatic code like:

```python
bot = BotManager.objects.get(name='SupportBot')
bot.sendMessage(chat_id=user_id, text='Welcome!')
```

Combined with the Typography approach, Monogram keeps the API familiar to anyone who has read the Telegram Bot API documentation while fitting naturally into Django’s ORM and webhook handling.
