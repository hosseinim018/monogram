from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json
from monogram.bot.config import UPDATE_HANDLER
from monogram.bot.UpdatingMessages.Update import Update


@csrf_exempt
def UpdateHandler(request):
    if request.method == 'POST':
        result = json.loads(request.body.decode('utf-8'))
        print(result)
        print('-------end result in views.py--------')
        if 'callback_query' in result:
            # run callback query functions
            for cqf in UPDATE_HANDLER['callback_query']:
                cqf(result['callback_query'])
        else:
            update = Update(**result)

            for message in UPDATE_HANDLER['message']:
                message(update.message)
        return HttpResponse("Hello, world!")
