
import re
from functools import wraps
from django.http import HttpResponse


def newMessage(pattern):
    def decorator(func):
        @wraps(func)
        def wrapper(Message, *args, **kwargs):
            if re.match(pattern, Message.text):
                return func(Message, *args, **kwargs)
            return HttpResponse("Hello, world!")
        return wrapper
    return decorator





