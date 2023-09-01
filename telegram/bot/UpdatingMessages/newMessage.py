import json, re
from functools import wraps
from django.http import HttpResponse

def newMessage(pattern):
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            if request.method == 'POST':
                result = json.loads(request.body.decode('utf-8'))
                text = result['message']['text']
                if re.match(pattern, text):
                    return func(request)
            return HttpResponse("Hello, world!")
        return wrapper
    return decorator