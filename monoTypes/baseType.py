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
