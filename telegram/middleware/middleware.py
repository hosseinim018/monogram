import json

class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Perform your request checking logic here
        if request.method == 'POST':
            result = json.loads(request.body.decode('utf-8'))
            headers = request.headers
            secret_token = headers['X-Telegram-Bot-Api-Secret-Token']

        response = self.get_response(request)
        # Perform any response processing here

        return response
