# Contributing

Thank you for considering contributing to Monogram. This guide explains how to keep the codebase consistent and how to add new API methods and types so they work correctly with `BotManager` and the rest of the stack.

---

## Principles

1. **Typography**: Follow the [Telegram Bot API](https://core.telegram.org/bots/api) documentation. Method names, parameter names, and type shapes should mirror the official API.
2. **Inheritance**: New Telegram types should inherit from `BaseType`; new API methods should live in `Methods` (and thus be available on every `BotManager` instance).
3. **Django compatibility**: Changes should remain compatible with Django’s ORM, migrations, and request/response cycle. Avoid breaking the webhook flow or the `BotManager` model contract.

---

## Adding a New Telegram Type

When the Telegram API introduces a new type (or you add support for an existing one):

1. **Create a new file** in `monoTypes/`, e.g. `NewType.py`.
2. **Inherit from `BaseType`** and match the API description:
   ```python
   from .baseType import BaseType

   class NewType(BaseType):
       def __init__(self, required_field: type, optional_field: type = None, **kwargs):
           super().__init__(**kwargs)
           self.required_field = required_field
           self.optional_field = optional_field
   ```
   - Use `super().__init__(**kwargs)` so extra/future keys are stored.
   - For nested objects, instantiate the corresponding type from `monoTypes` (e.g. `User(**data['from'])`).
3. **Export the type** in `monoTypes/__init__.py`:
   - Add `from .NewType import NewType`.
   - Add `"NewType"` to `__all__` if the package uses it.
4. **Use the type** where the API returns or consumes it (e.g. in `Update.py` for new update kinds, or in `methods.py` as a return type).

Do not introduce a parallel hierarchy or skip `BaseType`; keeping all types under `BaseType` preserves dict-like access and consistent behavior across the library.

---

## Adding a New API Method

New Telegram API methods should be implemented in `methods.py` so they are available on every `BotManager` instance.

1. **Open** [Telegram Bot API — Available methods](https://core.telegram.org/bots/api#available-methods) and find the method (e.g. `sendPhoto`).
2. **Add a method** on the `Methods` class with the same name and parameters as in the docs (camelCase is fine to match the API):
   ```python
   def sendPhoto(
       self,
       chat_id: Union[int, str],
       photo: Union[str, InputFile],
       caption: Optional[str] = None,
       return_response: bool = True,
       **kwargs
   ):
       payload = {
           'chat_id': chat_id,
           'photo': photo,
           'caption': caption,
           **kwargs
       }
       clean_payload = self._prepare_payload(payload)
       result = self.request(method="sendPhoto", payload=clean_payload,
                             return_response=return_response, files=...)
       return PhotoMessage(**result)  # or the appropriate type
   ```
3. **Use `self.request()`** for the HTTP call; do not bypass `Network.request()`.
4. **Return a typed object** when the API returns a known type (e.g. `Message`, `User`). If the method returns a raw value (e.g. boolean), return that.
5. **Optional `return_response`**: For consistency with existing methods, support `return_response=True` when you need the raw response (e.g. for `setWebhook`); otherwise return the parsed result.

Because `BotManager` subclasses `Methods`, any new method in `Methods` is automatically available as `bot_instance.newMethod(...)` without changes to `models.py`.

---

## Webhook and Update Handling

- **New update types**: If Telegram adds a new optional field to the [Update](https://core.telegram.org/bots/api#update) object (e.g. `some_new_field`), add a branch in `monoTypes/Update.py` to detect it and set the corresponding attribute to an instance of the right type (inheriting from `BaseType`).
- **Webhook view**: Prefer keeping `webhook.py` focused on: resolving bot by URL, verifying secret token, parsing JSON, building `Update(bot=bot, **update_data)`, and calling `_process_update`. Business logic should live in the bot class referenced by `bot.object`.

---

## Code Style and Quality

- **Type hints**: Use type hints for method parameters and return types where it helps readability and tooling.
- **Docstrings**: Document parameters and return values, especially for public methods in `methods.py` and constructors in `monoTypes/`.
- **Logging**: Use the existing `logger` in `network.py` and `webhook.py` for errors and important events; avoid `print()` for production behavior.
- **Tests**: If you add tests, ensure they run in the project’s Django test environment and do not depend on real Telegram tokens or external services when possible.

---

## Checklist for a Pull Request

- [ ] New types inherit from `BaseType` and are exported from `monoTypes/__init__.py` if needed.
- [ ] New API methods are implemented in `methods.py` and use `self.request()`.
- [ ] Method names and parameters align with the Telegram Bot API documentation.
- [ ] New Update variants are handled in `monoTypes/Update.py` with the correct typed class.
- [ ] No breaking changes to `BotManager`’s public behavior or to the webhook URL/response contract.
- [ ] Docstrings and type hints are updated where relevant.

Following these guidelines keeps the Typography structure intact and ensures new methods and types are available on `BotManager` and throughout the Django ecosystem.
