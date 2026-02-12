from monogram.text import format_text
from typing import Dict, Any

class BaseType:
    def __init__(self, *args, **kwargs):
        # Handle keyword arguments
        for key, value in kwargs.items():
            if key == 'from':
                key = 'from_user'
            self.__dict__[key] = value   

    def __getitem__(self, key):
        try:
            return self.__dict__[key]
        except KeyError:
            raise KeyError(f'Key {key} not found.')
        except Exception as e:
            raise e

    def __setitem__(self, key, value):
        try:
            self.__dict__[key] = value
        except Exception as e:
            raise e

    def __delitem__(self, key):
        try:
            del self.__dict__[key]
        except KeyError:
            raise KeyError(f'Key {key} not found.')
        except Exception as e:
            raise e

    def __contains__(self, key):
        try:
            return key in self.__dict__
        except Exception as e:
            raise e

    def __len__(self):
        try:
            return len(self.__dict__)
        except Exception as e:
            raise e

        try:
            return len(self.__dict__)
        except Exception as e:
            raise e

    def __repr__(self):
        try:
            return f'{self.__class__.__name__}({self.__dict__})'
        except Exception as e:
            raise e
    
    def _prepare_payload(self, raw_payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Prepares a payload dictionary for Telegram API requests.
        Removes None values and formats text/caption fields.

        Args:
            raw_payload: The dictionary of parameters for the API method.

        Returns:
            A cleaned and formatted payload dictionary.
        """
        if raw_payload:
            # Remove None values from payload
            payload = {k: v for k, v in raw_payload.items() if v is not None}

            if 'self' in payload:
                payload.pop('self')
            if 'cls' in payload:
                payload.pop('cls')
            # Apply text formatting if 'text' or 'caption' keys exist
            if 'text' in payload and payload['text'] is not None:
                payload['text'] = format_text(payload['text'])
            if 'caption' in payload and payload['caption'] is not None:
                payload['caption'] = format_text(payload['caption'])
                
            return payload
        return {}