from django.http import HttpResponse
from monogram.UpdatingMessages import Update
import json


def UpdateHandler(request, UPDATE_HANDLER):
    if request.method == 'POST' and UPDATE_HANDLER is not None:
        result = json.loads(request.body.decode('utf-8'))
        if 'callback_query' in result:
            # run callback query functions
            for cqf in UPDATE_HANDLER['callback_query']:
                cqf(result['callback_query'])
        else:
            update = Update(**result)

            for message in UPDATE_HANDLER['message']:
                message(update.message)
        return HttpResponse("Hello, world!")
