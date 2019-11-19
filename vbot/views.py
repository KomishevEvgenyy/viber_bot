#то что мы видим на сайте при запуске хоста
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import TextMessage, PictureMessage, KeyboardMessage, ContactMessage
from viberbot.api.viber_requests import *

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from .models import ViberUser



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
        if isinstance(viber_request, ViberMessageRequest): # фильтр подписки и отписки от viber
            #viber.send_messages(viber_request.sender.id, [TextMessage(text = "Вы подписаны на паблик")])
            #print(viber_request, ViberMessageRequest)
            if isinstance (viber_request.message, TextMessage): # фильтр текста выводит на консоль полученный текст и отправляет сообщение, что это картинка
                viber.send_messages(viber_request.sender.id, [TextMessage(text = 'Это текст')])
            elif isinstance (viber_request.message, PictureMessage): # фильтр картинки, выводит на консоль адрес картинки и отправляет сообщение, что это картинка
                viber.send_messages(viber_request.sender.id, [TextMessage(text = 'Это картинка')])
            elif isinstance(viber_request.message, ContactMessage):
                vuser = ViberUser.objects.get(viber_id=viber_request.sender.id)
                vuser.phone_number = viber_request.message.contact.phone_number
                vuser.save()
        elif isinstance(viber_request, ViberSubscribedRequest):

            user,create = ViberUser.objects.update_or_create(viber_id = viber_request.user.id, defaults={'is_active': True,
                                            'name': viber_request.user.name,
                                            'country': viber_request.user.country,
                                            'language': viber_request.user.language})
            if user.phone_number is None:
                SAMPLE_KEYBOARD = {
                    "Type": "keyboard",
                    "Buttons": [
                        {
                        "Columns": 6,
                        "Rows": 2,
                        "BgLoop": True,
                        "ActionType": "share-phone",
                        "ActionBody": "This will be sent to your bot in a callback",
                        "ReplyType": "message",
                        "Text": "<font color = ”# 7F00FF”> Push me! < font>"
                        }
                        ]
                }
                text_message = TextMessage(text = 'Номер принят')
                keyboard_message = KeyboardMessage(tracking_data='tracking_data', keyboard=SAMPLE_KEYBOARD, min_api_version=3)
                viber.send_messages(user.viber_id, [text_message, keyboard_message])

                #contact = Contact(name="Viber user", phone_number="+0015648979", avatar="http://link.to.avatar")
            #    contact_message = ContactMessage(contact=contact)
                    #vuser = ViberUser.objects.get(id=request.GET.get('user'))
                    #viber.send_messages(vuser.viber_id, [TextMessage(text=request.GET.get('text')),
                    #KeyboardMessage(tracking_data='tracking_data', keyboard=SAMPLE_KEYBOARD, min_api_version=3)])

        elif isinstance(viber_request, ViberUnsubscribedRequest):
            ViberUser.objects.update_or_create (viber_id=viber_request.user_id, defaults={'is_active': False})
            #elif isinstance (viber_request.message, PictureMessage): # доделать. должно выводить текс, что это видео
        #viber.send_messages(viber_request.sender.id, TextMessage(text = 'Hi')) # эхо бот. Отвечает на сообщение текстом Hi
        #if send_messages == True:
            #with open('massage_user.txt', 'br') as send_messages:
    return HttpResponse(status=200)

def send_message_for_user(request):
    SAMPLE_KEYBOARD = {
        "Type": "keyboard",
        "Buttons": [
        	{
        	"Columns": 6,
        	"Rows": 2,
        	"BgLoop": True,
        	"ActionType": "reply",
        	"ActionBody": "This will be sent to your bot in a callback",
        	"ReplyType": "message",
        	"Text": "<font color = ”# 7F00FF”> Push me! </ font>"
        	}
            ]
        }
    vuser = ViberUser.objects.get(id=request.GET.get('user'))
    viber.send_messages(vuser.viber_id, [TextMessage(text=request.GET.get('text')),
    KeyboardMessage(tracking_data='tracking_data', keyboard=SAMPLE_KEYBOARD, min_api_version=3)])
    return HttpResponse(status = 200)


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
