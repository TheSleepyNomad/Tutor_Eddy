from handlers.handler import Handler
from utils.utils import check_admin_role
from config.messages import MsgTemplates
from telebot.types import Message


class HandlerCommands(Handler):
    """
    Handle commands from user
    """

    def __init__(self, bot):
        super().__init__(bot)

    def pressed_start_btn(self, message: Message) -> None:
        """
        Handle the /start command
        """
        test = self.BD.get_all_lesson_records()
        print(test)
        # Check user in DB
        check_result = self.BD.check_user_on_exist_by_user_id(
            message.from_user.id)

        # check user role /admin/student/guest
        if check_admin_role(message.from_user.username):
            self.bot.send_message(message.chat.id, 'Админ вернулся!',
            reply_markup=self.keybords.admin_start_menu())

        else:
            # if user already in database
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
                self.bot.send_message(message.chat.id, f'{MsgTemplates.START_MSG}')

                # send msg for choosing language
                self.bot.send_message(message.chat.id,
                                    f'{MsgTemplates.CHOOSE_LANG_MSG}',
                                    reply_markup=self.keybords.choose_language_menu())

    def pressed_help_btn(self, message: Message) -> None:
        """
        Handle the /help command
        """
        self.bot.send_message(message.chat.id,
                              f'{MsgTemplates.HELP_MSG}')

    def pressed_about_btn(self, message: Message) -> None:
        """
        Handle the /about command
        """
        self.bot.send_message(message.chat.id,
                              f'{MsgTemplates.ABOUT_APP_MSG}')

    def handle(self):
        @self.bot.message_handler(commands=['start', 'help', 'about'])
        def handle(message: Message):

            if message.text == '/start':
                self.pressed_start_btn(message)

            if message.text == '/help':
                self.pressed_help_btn(message)

            if message.text == '/about':
                self.pressed_about_btn(message)
