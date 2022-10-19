from handlers.handler import Handler
from utils.utils import check_admin_role
from config.messages import MsgTemplates


class HandlerCommands(Handler):
    """
    Handle commands from user
    """

    def __init__(self, bot):
        super().__init__(bot)

    def pressed_start_btn(self, message) -> None:
        """
        Handle the /start command
        """
        # check user role /admin/student/guest
        # if check_admin_role(message.from_user.username):
        #     self.bot.send_message(message.chat.id, 'Админ вернулся!',
        #     reply_markup=self.keybords.admin_start_menu())

        # else:
        # if user already 'speak' with bot
        check_result = self.BD.check_user_on_exist_by_user_id(
            message.from_user.id)

        # if user not first time chat with bot
        if check_result:

            # if user is student
            if not check_result.guest_is:
                self.bot.send_message(message.chat.id,
                                      f'{MsgTemplates.STUDENTS_START_MSG}',
                                      reply_markup=self.keybords.students_start_menu())
            # if user still guest
            else:
                self.bot.send_message(message.chat.id,
                                      f'{MsgTemplates.GUEST_START_MSG}',
                                      reply_markup=self.keybords.guest_start_menu())
        # for new visitors
        else:
            # send welcome msg
            self.bot.send_message(message.chat.id,
                                  f'{MsgTemplates.START_MSG}')
            # reg user like guest
            self.BD._add_new_student(message.from_user.username,
                                     message.from_user.id,
                                     message.from_user.first_name,
                                     message.from_user.last_name)

            self.bot.send_message(message.chat.id,
                                  f'{MsgTemplates.GUEST_START_MSG}',
                                  reply_markup=self.keybords.guest_start_menu())

    def pressed_help_btn(self, message) -> None:
        """
        Handle the /help command
        """
        self.bot.send_message(message.chat.id,
                              f'{MsgTemplates.HELP_MSG}')

    def pressed_about_btn(self, message) -> None:
        """
        Handle the /about command
        """
        self.bot.send_message(message.chat.id,
                              f'{MsgTemplates.ABOUT_APP_MSG}')

    def handle(self):
        @self.bot.message_handler(commands=['start', 'help', 'about'])
        def handle(message):
            
            if message.text == '/start':
                self.pressed_start_btn(message)

            if message.text == '/help':
                self.pressed_help_btn(message)

            if message.text == '/about':
                self.pressed_about_btn(message)
