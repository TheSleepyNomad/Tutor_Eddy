from handlers.handler import Handler
from utils.utils import check_admin_role


class HandlerCommands(Handler):

    def __init__(self, bot):
        super().__init__(bot)

    def pressed_start_btn(self, message) -> None:
        # Проверяем кто пишет боту
        # if check_admin_role(message.from_user.username):
        #     self.bot.send_message(message.chat.id, 'Админ вернулся!',
        #     reply_markup=self.keybords.admin_start_menu())
            
        # else:
        # if user already 'speak' with bot
        check_result = self.BD.check_user_on_exist_by_user_id(
            message.from_user.id)
        if check_result:
            if not check_result.guest_is:
                self.bot.send_message(message.chat.id,
                                    f'{message.from_user.first_name},'
                                    f' здравствуйте! Теперь Вы студент!!!',
                                    reply_markup=self.keybords.students_start_menu())
            else:
                self.bot.send_message(message.chat.id,
                                f'{message.from_user.first_name},'
                                f' здравствуйте! Жду дальнейших задач.',
                                reply_markup=self.keybords.guest_start_menu())
            # load students menu
        else:
            # For new students
            self.BD._add_new_student(message.from_user.username,
                                    message.from_user.id,
                                    message.from_user.first_name,
                                    message.from_user.last_name)
            self.bot.send_message(message.chat.id,
                                f'{message.from_user.first_name},'
                                f' здравствуйте!',
                                reply_markup=self.keybords.guest_start_menu())
        # load new_students_menu

    def handle(self):
        @self.bot.message_handler(commands=['start', 'help', 'about'])
        def handle(message):
            if message.text == '/start':
                self.pressed_start_btn(message)

            if message.text == '/help':
                pass
            if message.text == '/about':
                pass
