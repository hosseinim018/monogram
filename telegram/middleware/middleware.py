import json
from telegram.bot.config import SECRET_TOKEN

class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Perform your request checking logic here
        if request.method == 'POST':
            # result = json.loads(request.body.decode('utf-8'))
            headers = request.headers
            secret_token = headers['X-Telegram-Bot-Api-Secret-Token']
            if secret_token == SECRET_TOKEN:
                response = self.get_response(request)
                # Perform any response processing here
                # print('SECRET_TOKEN is valid')
                return response
            else:
                raise Exception('SECRET_TOKEN is not valid')

