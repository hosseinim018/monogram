from django.http import HttpResponse
from monogram.UpdatingMessages import Update
from monogram.types import CallbackQuery
import json
from pprint import pprint

def UpdateHandler(request, UPDATE_HANDLER):
    if request.method == 'POST' and UPDATE_HANDLER is not None:
        result = json.loads(request.body.decode('utf-8'))
        # pprint(result)
        # if 'callback_query' in result:
        #     # run callback query functions
        #     for cqf in UPDATE_HANDLER['callback_query']:
        #         # result['from_user'] = result['callback_query']
        #         # cqf(CallbackQuery(result['callback_query']))
        #         cqf(result['callback_query'])
        # else:
        update = Update(**result)
        if 'callback_query' in result:
            for cqf in UPDATE_HANDLER['callback_query']:
                cqf(update.callback_query)
        elif 'message' in result:
            for message in UPDATE_HANDLER['message']:
                message(update.message)
        else:
            pass
        return HttpResponse("Hello, world!")
