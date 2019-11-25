from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import TextMessage, PictureMessage, KeyboardMessage, ContactMessage
from viberbot.api.viber_requests import *


from .models import ViberUser

viber = Api(BotConfiguration(
    name='Bot',
    avatar='',
    auth_token='4a89a494ec67d4d8-ce1705a5075c3ee5-1adcf91592112c94'
))

def registration(v_id):
    v_user, create = ViberUser.objects.update_or_create(viber_id=v_id, defaults={'is_active': True})
    if v_user.phone_number is None:
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
        viber.send_messages(vuser.viber_id, [text_message, keyboard_message])
