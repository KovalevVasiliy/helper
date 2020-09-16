import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent

from settings import Settings


class VkSender:
    def check_message(self, message):
        appeals = [
            'Уважаемые магистранты',
            'Уважаемые студенты',
            'Уважаемые старосты'
        ]
        for ap in appeals:
            if ap in message:
                return True
        return False

    def run(self):
        vk_session = vk_api.VkApi(token=Settings.VK_APP_KEY)
        vk = vk_session.get_api()
        longpoll = VkBotLongPoll(vk_session, Settings.VK_GROUP)
        vk = vk_session.get_api()
        event: VkBotMessageEvent
        for event in longpoll.listen():
            print(1)
            if event.type == VkBotEventType.MESSAGE_NEW and event.message:
                print(2)
                if event.from_chat:  # Если написали в Беседе
                    print(3)
                    if self.check_message(event.message['text']):
                        print(4)
                        vk.messages.send(  # ответ
                            chat_id=event.chat_id,
                            message='Передал 20ИМ',
                            random_id=get_random_id()
                        )

                        vk.messages.send(  # ответ
                            chat_id=Settings.VK_TO_GROUP_ID,
                            message="Сообщение от деканата!\n" + event.message['text'],
                            random_id=get_random_id()
                        )
                        print(5)

