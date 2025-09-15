from django.shortcuts import render
from django.views import View
from django.http import request, JsonResponse
from .models import BotManager
# Create your views here.

def response_generator(message, status, code,data=None):
    response = {
        'message': message,
        'status': status,
        'code': code,
    }
    if data:
        response['data'] = data
    return response

def get_list_bots(request):
    try:
        bots = BotManager.objects.all().values_list
        reponse = response_generator(message='list of bots', status='success', code=200, data=bots)
        return JsonResponse(reponse)
    except:
        reponse = response_generator(message='erorr in get list of bots from botmanager model', status='error', code=400)
        return JsonResponse(reponse)
    

