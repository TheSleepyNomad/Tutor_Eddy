from handlers.handler import Handler
from utils.utils import check_admin_role


class HandlerCommands(Handler):

    def __init__(self, bot):
        super().__init__(bot)

    def pressed_start_btn(self, message) -> None:
        # Проверяем кто пишет боту
        # if check_admin_role(message.from_user.username):
        #     self.bot.send_message(message.chat.id, 'Админ вернулся!')
        # else:
        self.bot.send_message(message.chat.id,
                              f'{message.from_user.first_name},'
                              f' здравствуйте! Жду дальнейших задач.')

    def handle(self):
        @self.bot.message_handler(commands=['start', 'help', 'about'])
        def handle(message):
            if message.text == '/start':
                print(type(message))
                self.pressed_start_btn(message)

            if message.text == '/help':
                pass
            if message.text == '/about':
                pass
