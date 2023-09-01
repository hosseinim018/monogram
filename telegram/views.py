from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from telegram.bot.UpdatingMessages.newMessage import newMessage
import json
from .sendMessage import send_message




@csrf_exempt
@newMessage(pattern=r'^/start$')
def bot(request):
    result = json.loads(request.body.decode('utf-8'))
    print(result)
    chat_id = result['message']['chat']['id']
    text = result['message']['text']
    print(chat_id, text)
    send_message(chat_id=chat_id, text=text)
    return HttpResponse("Hello, world!")
