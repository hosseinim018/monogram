# Monogram

<div align="center">

**A Typography-based Telegram Framework for Django**

*Build scalable Telegram bots with a Django-native, type-safe API that mirrors the official Telegram Bot API.*

</div>

---

## ✨ What is Monogram?

<<<<<<< HEAD
Monogram is a **Django-based Telegram Bot library** that uses **webhooks** to receive updates. It follows a *Typography* approach: method names, parameters, and types align with the [official Telegram Bot API](https://core.telegram.org/bots/api), so you work with familiar concepts and a clean, predictable surface. Every bot is a **Django model**—stored in the DB, manageable via admin or custom views, and ready to scale within the Django ecosystem.

---

## 🎯 The "Miracle": BotManager

**BotManager** bridges the gap between **Django Models** and **Telegram Methods**. Each bot is a single model instance that *is also* the API client—no separate client object to hold or pass around.

```python
from monogram.models import BotManager

# Load your bot from the database
bot = BotManager.objects.get(name='SupportBot')

# Call Telegram methods directly on the model instance
bot.sendMessage(chat_id=user_id, text='Hello!')
me = bot.getMe()
```

You get **`bot_instance.sendMessage()`** (and every other API method) because `BotManager` inherits from **Methods**, which implements the full Telegram API. The same object is your persisted bot configuration and your live client. Credentials stay in sync: when you change the token and save, the instance is reinitialized with the new settings.

---

## 🔗 The Typography Chain

Under the hood, Monogram is built on a simple inheritance chain that gives every bot its power:

| Layer | Role |
|-------|------|
| **Network** (`network.py`) | HTTP client: requests, sessions, payload handling, file download. |
| **Methods** (`methods.py`) | Telegram API methods (e.g. `sendMessage`, `getMe`, `setWebhook`) and typed returns. |
| **BotManager** (`models.py`) | Django model + Methods → one bot = one model instance. |

**Network → Methods → BotManager.** Each layer adds responsibility; by the time you use a `BotManager` instance, you have the full API at your fingertips.

---

## 🚀 Quickstart

### 1. Install

```bash
pip install monogram
```
=======
You can install Monogram using one of the following methods:

1. **Using pip**:
   ```bash
   pip install monogram
   ```

2. **Cloning the Repository**:
   ```bash
   git clone https://github.com/hosseinim018/monogram.git
   ```
   Add Monogram to your Django project manually after cloning.
---
>>>>>>> 8f5ba1edfc9494d5db328225218355a0dc1768f0

### 2. Configure Django

Add `monogram` to `INSTALLED_APPS` and set your public domain for webhooks:

```python
# settings.py
INSTALLED_APPS = [
    # ...
    'monogram',
]

DOMAIN_NAME = "your-domain.com"  # Used for webhook URLs (e.g. https://your-domain.com/monogram/...)
```

Include Monogram URLs:

```python
# urls.py
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('monogram/', include('monogram.urls')),
]
```

### 3. Migrate and add your bot

```bash
python manage.py migrate
```

Open `https://your-domain.com/monogram/` in the browser, add your bot (name + token), then set the webhook for that bot. In the bot’s settings, set **Object** to the dotted path of your bot class (e.g. `myapp.bot.MyBot`).

### 4. Define your bot logic class

Your class receives the **bot** (`BotManager` instance) and a typed **Update** from `monoTypes`. Use them to send messages, read `update.message`, handle callbacks, etc.

```python
# myapp/bot.py
from monogram.models import BotManager
from monogram.monoTypes import Update

class MyBot:
    """Bot logic: receives (bot, update); use typed Update and bot.sendMessage()."""

    def __init__(self, bot: BotManager, update: Update):
        self.bot = bot
        self.update = update
        self.handle_update()

    def handle_update(self):
        # Typed update: .message, .callback_query, .inline_query, etc.
        if 'message' in self.update:
            msg = self.update.message
            chat_id = msg.chat.id
            text = getattr(msg, 'text', '') or ''
            self.bot.sendMessage(chat_id=chat_id, text=f"You said: {text}")
```

Set **Object** for this bot in the Monogram UI to `myapp.bot.MyBot`. When a webhook arrives, Monogram loads that class, instantiates `MyBot(bot, update)`, and your handler runs with a typed `Update` and direct access to `bot.sendMessage()` and the rest of the API.

### 5. Run the server

```bash
python manage.py runserver
```

Use a public URL (or a tunnel like ngrok) for webhooks so Telegram can reach your app.

---

## 🌟 Feature Highlights

| Feature | Description |
|--------|-------------|
| **📐 Strict type mapping** | Incoming/outgoing data is mapped to `monoTypes` (`Update`, `Message`, `User`, `Chat`, …) so you work with objects, not raw dicts. |
| **📈 Scalable bot management** | Multiple bots as Django model rows; manage tokens, webhooks, and handler paths per bot. |
| **🔌 Seamless Django integration** | Webhooks are Django views; bots are models; use Django auth, DB, and deployment as usual. |
| **📖 Typography design** | Method and type names follow the [Telegram Bot API](https://core.telegram.org/bots/api); easy to extend and keep in sync with the docs. |
| **🔒 Webhook security** | Optional secret token verification via `X-Telegram-Bot-Api-Secret-Token` header. |
| **🌐 Webhook-based** | No long polling; Telegram pushes updates to your HTTPS endpoint. |

---

## 📚 Wiki & Deep Dives

For architecture, type system, webhook flow, and contributing guidelines, see the **GitHub Wiki**:

- [**Home**](https://github.com/YOUR_USERNAME/monogram/wiki/Home) — Overview and Typography philosophy  
- [**Architecture**](https://github.com/YOUR_USERNAME/monogram/wiki/Architecture) — Network → Methods → BotManager and Mermaid diagram  
- [**Type system**](https://github.com/YOUR_USERNAME/monogram/wiki/Type-System) — `monoTypes` and `BaseType`  
- [**Webhook handling**](https://github.com/YOUR_USERNAME/monogram/wiki/Webhook-Handling) — How updates are routed and converted to typed `Update`  
- [**Contributing**](https://github.com/YOUR_USERNAME/monogram/wiki/Contributing) — How to add types and methods and keep the structure consistent  

Replace `YOUR_USERNAME` with your GitHub username or org.

---

## 🤝 Contributing

Contributions are welcome. To keep the project consistent:

- **Typography**: Follow the [Telegram Bot API](https://core.telegram.org/bots/api) for method and type names.
- **Types**: New Telegram types should inherit from `BaseType` in `monoTypes/` and be exported in `monoTypes/__init__.py`.
- **Methods**: New API methods go in `methods.py` so they are available on every `BotManager` instance.
- **Django**: Preserve the webhook flow and the `BotManager` model contract.

See the [Contributing wiki page](https://github.com/YOUR_USERNAME/monogram/wiki/Contributing) for the full guide (adding types, adding methods, PR checklist).

1. Fork the repo  
2. Create a branch for your feature or fix  
3. Submit a pull request with a clear description of your changes  

---

> **Note:** Monogram is currently in **beta**. If you hit issues or have ideas, please open an issue or PR.

Thank you for using Monogram.
