#то что мы видим на сайте при запуске хоста
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import TextMessage, PictureMessage

from viberbot.api.viber_requests import *
from .models import ViberUser


from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings



viber = Api(BotConfiguration(
    name='Bot',
    avatar='',
    auth_token='4a89a494ec67d4d8-ce1705a5075c3ee5-1adcf91592112c94'
))

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        viber_request = viber.parse_request(request.body)
        if isinstance(viber_request, ViberMessageRequest): # фильтр подписки и отписки от viber
            #viber.send_messages(viber_request.sender.id, [TextMessage(text = "Вы подписаны на паблик")])
            #print(viber_request, ViberMessageRequest)
            if isinstance (viber_request.message, TextMessage): # фильтр текста выводит на консоль полученный текст и отправляет сообщение, что это картинка
                viber.send_messages(viber_request.sender.id, [TextMessage(text = 'Это текст')])
            elif isinstance (viber_request.message, PictureMessage): # фильтр картинки, выводит на консоль адрес картинки и отправляет сообщение, что это картинка
                viber.send_messages(viber_request.sender.id, [TextMessage(text = 'Это картинка')])
        elif isinstance(viber_request, ViberSubscribedRequest):
            ViberUser.objects.update_or_create(viber_id = viber_request.user.id, defaults={'is_active': True,
                                            'name': viber_request.user.name,
                                            'country': viber_request.user.country,
                                            #'is_active': viber_request.user.is_active,
                                            'language': viber_request.user.language})
        elif isinstance(viber_request, ViberUnsubscribedRequest):
            ViberUser.objects.update_or_create (viber_id=viber_request.user_id, defaults={'is_active': False})
            #elif isinstance (viber_request.message, PictureMessage): # доделать. должно выводить текс, что это видео
        #viber.send_messages(viber_request.sender.id, TextMessage(text = 'Hi')) # эхо бот. Отвечает на сообщение текстом Hi
        #if send_messages == True:
            #with open('massage_user.txt', 'br') as send_messages:
    return HttpResponse(status=200)

@csrf_exempt
def set_webhook(request):
    event_types = [
      "failed",
      "subscribed", # дает право писать и создавать user
      "unsubscribed", # получаем id и time
      "conversation_started",
      "messages",
      ]
    url = f'https://{settings.ALLOWED_HOSTS[0]}/vbot/callback/'
    viber.set_webhook(url = url, webhook_events = event_types) # дает возможность включить чат в viber
    return HttpResponse('Ok')

@csrf_exempt
def unset_webhook(request):
    viber.unset_webhook()# отключает чат в viber
    return HttpResponse("webhook drop")


# Create your views here.
