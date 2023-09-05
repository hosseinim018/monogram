from django.http import HttpResponse
import json, re
from functools import wraps
# from telegram.bot.UpdatingMessages import deleteMessage, editMessageCaption, editMessageText, editMessageMedia, \
#     editMessageLiveLocation, editMessageReplyMarkup, stopMessageLiveLocation, stopPoll
def newMessage(pattern):
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            if request.method == 'POST':
                result = json.loads(request.body.decode('utf-8'))
                if 'callback_query' in result:
                    print((result))
                    print('callback_query come')
                    print(result['callback_query'])
                else:
                    text = result['message']['text']
                    if re.match(pattern, text):
                        return func(request, *args, **kwargs)

            return HttpResponse("Hello, world!")
        return wrapper
    return decorator