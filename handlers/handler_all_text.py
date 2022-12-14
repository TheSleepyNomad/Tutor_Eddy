from handlers.handler import Handler
from config.settings import KEYBOARD
from config.messages import MsgTemplates
from telebot.types import Message


class HandlerAllText(Handler):
    """
    Handle button from user keyboard
    """

    def __init__(self, bot):
        super().__init__(bot)

    def pressed_help_btn(self, message: Message) -> None:
        """
        handle help btn
        """
        self.bot.send_message(message.chat.id,
                              f'{MsgTemplates.HELP_MSG}')

    def pressed_about_app_btn(self, message: Message) -> None:
        """
        handle about app btn
        """
        self.bot.send_message(message.chat.id,
                              f'{MsgTemplates.ABOUT_APP_MSG}')

    def pressed_about_tutor_btn(self, message: Message) -> None:
        """
        handle about tutor btn
        """
        self.bot.send_message(message.chat.id,
                              f'{MsgTemplates.ABOUT_TUTOR_MSG}')

    def pressed_test_lesson_btn(self, message: Message) -> None:
        """
        handle btn for extended inforamtion about lessons
        """
        # guest = self.BD.check_user_on_exist_by_user_id(message.chat.id)
        # lesson = self.BD.get_guest_lesson_by_user_id(guest.id)
        # if lesson:
        #     self.bot.send_message(message.chat.id,
        #                           f'Вы уже записаны на занятие')
        # else:
        self.bot.send_message(message.chat.id,
                              f'{MsgTemplates.ABOUT_LESSONS_MSG}',
                              reply_markup=self.keybords.guest_lesson_menu())
        self.keybords.remove_menu()


    def pressed_back_btn(self, message: Message) -> None:
        """
        handle return back btn
        """
        self.bot.send_message(message.chat.id, "Вы вернулись назад",
                              reply_markup=self.keybords.guest_start_menu())

    def pressed_rus_lang_btn(self, message: Message) -> None:
        """
        handle rus lang btn in language menu
        """
        self.bot.send_message(message.chat.id, "Выбран русский язык")
        # send msg and get user phone
        self.bot.send_message(message.chat.id,
                              f'{MsgTemplates.SET_USR_SETTING}',
                              reply_markup=self.keybords.get_user_phone())

    def pressed_eng_lang_btn(self, message: Message) -> None:
        """
        handle eng lang btn in language menu
        """
        self.bot.send_message(message.chat.id, "Все равно будет русский =)")
        # send msg and get user phone
        self.bot.send_message(message.chat.id,
                              f'{MsgTemplates.SET_USR_SETTING}',
                              reply_markup=self.keybords.get_user_phone())

    def handle(self) -> None:
        
        @self.bot.message_handler(func=lambda message: True)
        def handle(message: Message) -> None:
            # ---- menu btns -----
            # admin keyboard btns
            if message.text == KEYBOARD['LESSONS']:
                pass

            if message.text == KEYBOARD['ADD_STUDENT']:
                pass

            # student keyboard btns
            if message.text == KEYBOARD['MY_LESSONS']:
                pass

            # guest keyboard btns
            if message.text == KEYBOARD['TEST_LESSON']:
                self.pressed_test_lesson_btn(message)

            # other btns
            if message.text == KEYBOARD['ABOUT_TUTOR']:
                self.pressed_about_tutor_btn(message)

            if message.text == KEYBOARD['ABOUT_APP']:
                self.pressed_about_app_btn(message)

            if message.text == KEYBOARD['SETTINGS']:
                pass

            if message.text == KEYBOARD['HELP']:
                self.pressed_help_btn(message)

            if message.text == KEYBOARD['RUS']:
                self.pressed_rus_lang_btn(message)

            if message.text == KEYBOARD['ENG']:
                self.pressed_eng_lang_btn(message)

            if message.text == KEYBOARD['<<']:
                self.pressed_back_btn(message)
