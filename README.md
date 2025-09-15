# Monogram

Monogram is a powerful and flexible Django library designed to help developers build scalable Telegram bots with ease. Whether you're a beginner or an experienced developer, Monogram provides the tools you need to create robust and feature-rich bots.

## Features

- **Bot Manager**: Manage your bots effortlessly with Monogram's intuitive bot management system.
- **Security and Middleware**: Built-in security features and middleware for seamless integration.
- **Webhook-Based**: Efficient and reliable webhook support for real-time updates.
- **Ease of Use**: Simple and developer-friendly API for quick implementation.
- **Scalable and Extendable**: Designed to scale and adapt to your needs, making it suitable for everyone.

> **Warning**: Monogram is currently in beta. If you encounter any issues or have new ideas, please report them!

---

## Installation

To install Monogram, simply use pip:

```bash
pip install monogram
```
---

## Quickstart

Here’s how you can get started with Monogram:

1. **Create a Django App**:
   ```bash
   django-admin startapp mybot
   ```

2. **Install Monogram**:
   1. Add `monogram` to your `INSTALLED_APPS` in `settings.py`.
   2. add `DOMAIN_NAME` to `settings.py`:
   ```python
        DOMAIN_NAME = "046ef5be639f.ngrok-free.app" #for monogram webhook
    ```

3. add `monogram.urls` to your project's `urls.py`:

   ```python
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('monogram/', include('monogram.urls')),
   ]
   ```
4. in your browser go to your-domain/monogram/ path and add your bot token and setwebook

5. **Create Your Bot**:
   Define your bot by extending the `Dispatcher` class:
   ```python
   from monogram import Dispatcher

   class MyBot(Dispatcher):
       def handle_update(self, update):
           self.bot.sendMessage(
               chat_id=update.message.chat.id,
               text="Hello, this is my bot!"
           )
   ```

6. **Run Your Bot**:
   Before starting your bot, make sure to apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
   Then, use Django's `runserver` to start your bot:
   ```bash
   python manage.py runserver
   ```

---

## Next Steps

- **Examples**: Check out the [examples](examples/) directory for more use cases.
- **Documentation**: Read the full documentation [here](documants/).
- **Advanced Features**: Learn about advanced features like middlewares, custom handlers, and more.

---

## Contributing

We welcome contributions from the community! Here’s how you can help:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

---

Thank you for using Monogram! 🚀
