# Type System

## Overview

The `monoTypes/` directory contains Python classes that mirror the [Telegram Bot API types](https://core.telegram.org/bots/api#available-types). Every type inherits from `BaseType`, which provides a consistent way to build objects from API JSON and to access fields by attribute or key. This keeps the codebase aligned with the official API and makes it straightforward to add or update types when Telegram’s documentation changes.

---

## BaseType (`monoTypes/baseType.py`)

All Telegram types derive from `BaseType`:

```python
class BaseType:
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            if key == 'from':
                key = 'from_user'
            self.__dict__[key] = value

    def __getitem__(self, key): ...
    def __setitem__(self, key, value): ...
    def __delitem__(self, key): ...
    def __contains__(self, key): ...
    def __len__(self): ...
    def __repr__(self): ...
```

**Behavior:**

- **Keyword-based construction**: Any keyword argument is stored on the instance (with `from` renamed to `from_user` to avoid a Python keyword). This allows `User(**api_dict)` or `Message(**api_dict)` from raw API payloads.
- **Dict-like access**: Types support `obj['field']`, `obj['field'] = value`, `'field' in obj`, and `len(obj)`, so they can be used like dictionaries where needed while still exposing attributes.
- **Single source of shape**: The set of attributes is defined by the JSON keys passed in (and any explicit attributes set in subclasses). There is no separate schema definition; the class plus the API docs define the shape.

By inheriting from `BaseType`, every type in `monoTypes/` gets this behavior and stays consistent with the rest of the library.

---

## Structure of `monoTypes/`

The directory is organized by Telegram’s type names, with one module per type (or small group of related types). Examples:

- **Core**: `User`, `Chat`, `Message`, `Update`
- **Media**: `PhotoSize`, `Audio`, `Document`, `Video`, `Voice`, `Animation`, `VideoNote`
- **Inline**: `InlineQuery`, `InlineKeyboardMarkup`, `InlineKeyboardButton`, `InlineQueryResult*`
- **Chat**: `ChatMember`, `ChatMemberUpdated`, `ChatJoinRequest`, `ChatPermissions`, etc.
- **Payments & business**: `Invoice`, `SuccessfulPayment`, `BusinessConnection`, etc.
- **Other**: `Poll`, `Location`, `File`, `WebAppInfo`, and many more.

Each type module typically:

1. Imports `BaseType` (from `.baseType` or `monogram.monoTypes.baseType`).
2. Defines a class that subclasses `BaseType`.
3. Implements `__init__(self, **kwargs)` and calls `super().__init__(**kwargs)`, then may set specific attributes or parse nested objects into other `monoTypes` classes.

`monoTypes/__init__.py` re-exports these types so the rest of the app can do:

```python
from monogram.monoTypes import Update, Message, User, Chat
```

---

## Example: User

`User` mirrors the [User](https://core.telegram.org/bots/api#user) type and shows the usual pattern: inherit from `BaseType`, call `super().__init__(**kwargs)`, then set known fields explicitly for clarity and type hints:

```python
# monoTypes/User.py
from .baseType import BaseType

class User(BaseType):
    def __init__(self, id: int, is_bot: bool, first_name: str,
                 last_name: Optional[str] = None,
                 username: Optional[str] = None,
                 language_code: Optional[str] = None,
                 is_premium: Optional[bool] = None,
                 # ... other optional fields
                 *args, **kwargs):
        super().__init__(**kwargs)
        self.id = id
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        # ...
```

Required and optional fields follow the Telegram docs; extra keys from the API are still stored via `super().__init__(**kwargs)`.

---

## Example: Update (nested typing)

`Update` is the root object for an incoming webhook payload. It has a single `update_id` and exactly one of many optional fields (`message`, `edited_message`, `callback_query`, etc.). The type parses the raw JSON and instantiates the correct nested type for whichever key is present:

```python
# monoTypes/Update.py (simplified)
class Update(BaseType):
    def __init__(self, bot, **kwargs):
        super().__init__(**kwargs)
        if 'message' in self:
            self.message = Message(bot=bot, **self['message'])
        elif 'edited_message' in self:
            self.edited_message = Message(bot=bot, **self['edited_message'])
        elif 'callback_query' in self:
            callback_data = self['callback_query']
            if 'message' in callback_data and isinstance(callback_data['message'], dict):
                callback_data['message'] = Message(bot=bot, **callback_data['message'])
            self.callback_query = CallbackQuery(bot=bot, **callback_data)
        elif 'inline_query' in self:
            self.inline_query = InlineQuery(**self['inline_query'])
        # ... other branches for channel_post, poll, chat_member, etc.
```

So the incoming JSON is turned into one typed `Update` with one of its attributes set to a typed `Message`, `CallbackQuery`, `InlineQuery`, etc. This is how webhook handlers receive structured, typed objects instead of raw dicts.

---

## Adding a New Telegram Type

To add a new type that appears in the [Telegram Bot API](https://core.telegram.org/bots/api#available-types):

1. **Create a new file** in `monoTypes/`, e.g. `NewType.py`.
2. **Define a class that inherits from `BaseType`** and matches the API description:
   - In `__init__`, accept the fields listed in the docs (required and optional).
   - Call `super().__init__(**kwargs)` so any extra or future keys are stored.
   - Set `self.<field> = ...` for the fields you care about; for nested objects, instantiate the corresponding `monoTypes` class (e.g. `User(**self['from'])`).
3. **Export the type** in `monoTypes/__init__.py`:
   - `from .NewType import NewType`
   - Add `"NewType"` to `__all__` (if used).
4. **Use it** where the API returns or expects that type (e.g. in `Update`, in a method in `methods.py` that returns a typed result).

No separate schema or code generator is required: if the Telegram docs describe a type, you add a class that matches that description and inherits from `BaseType`. The Typography approach is exactly this: one class per API type, shaped by the official documentation.

---

## Summary

| Concept | Detail |
|--------|--------|
| **Base class** | Every type in `monoTypes/` inherits from `BaseType`. |
| **Construction** | Types are built from keyword arguments (e.g. API JSON), with `from` → `from_user`. |
| **Access** | Attribute access and dict-like `[]` access are both supported. |
| **Nesting** | Complex types (e.g. `Update`, `Message`) construct nested types explicitly in `__init__`. |
| **Extending** | New API types = new class in `monoTypes/` inheriting from `BaseType`, following the Telegram docs. |

The type system keeps the library aligned with the Telegram Bot API and keeps adding or updating types a matter of adding or editing a single class that mirrors the documentation.
