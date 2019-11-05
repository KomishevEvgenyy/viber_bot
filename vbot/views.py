#то что мы видим на сайте при запуске хоста
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import TextMessage

from viberbot.api.viber_requests import ViberMessageRequest

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

viber = Api(BotConfiguration(
    name='Bot',
    avatar='',
    auth_token='4a89a494ec67d4d8-ce1705a5075c3ee5-1adcf91592112c94'
))

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        viber_request = viber.parse_request(request.body)
        print(viber_request)
        viber.send_messages(viber_request.sender.id, TextMessage(text = 'Hi')) # эхо бот. Отвечает на сообщение текстом Hi
        #if send_messages == True:
            #with open('massage_user.txt', 'br') as send_messages:


    return HttpResponse(status=200)


# Create your views here.
