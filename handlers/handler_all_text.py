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
                              reply_markup=self.keybords.set_guest_menu())
        self.keybords.remove_menu()

    def pressed_back_btn(self, message: Message) -> None:
        """
        handle return back btn
        """
        user_role = self.BD.check_user_role(message.from_user.id)
        if user_role == 'admin':
            self.bot.send_message(message.chat.id, "Вы вернулись назад",
                                  reply_markup=self.keybords.set_admin_menu())

        if user_role == 'student':
            self.bot.send_message(message.chat.id, "Вы вернулись назад",
                                  reply_markup=self.keybords.set_students_menu())

        if user_role == 'guest':
            self.bot.send_message(message.chat.id, "Вы вернулись назад",
                                  reply_markup=self.keybords.set_guest_menu())

    def pressed_rus_lang_btn(self, message: Message) -> None:
        """
        handle rus lang btn in language menu
        """
        self.bot.send_message(message.chat.id, "Выбран русский язык")
        # send msg and get user phone
        self.bot.send_message(message.chat.id,
                              f'{MsgTemplates.SET_USR_SETTING}',
                              reply_markup=self.keybords.set_request_phone_menu())

    def pressed_eng_lang_btn(self, message: Message) -> None:
        """
        handle eng lang btn in language menu
        """
        self.bot.send_message(message.chat.id, "Все равно будет русский =)")
        # send msg and get user phone
        self.bot.send_message(message.chat.id,
                              f'{MsgTemplates.SET_USR_SETTING}',
                              reply_markup=self.keybords.set_request_phone_menu())

    def show_all_lessons(self, message: Message) -> None:
        list_of_records = self.BD.select_all_lessons()
        self.bot.send_message(message.chat.id,
                              f'Все уроки',
                              reply_markup=self.keybords.set_lessons_inline_menu(list_of_records))

    def show_admin_lessons_menu(self, message: Message) -> None:
        self.bot.send_message(message.chat.id,
                              f'Вы перешли в меню записей',
                              reply_markup=self.keybords.set_admin_lesson_action_menu())

    def add_new_lesson(self, message: Message) -> None:
        self.bot.send_message(message.chat.id,
                              f'По какому предмету делаем запись?',
                              reply_markup=self.keybords.set_list_of_lessons_for_add_lesson())

    def pressed_settings_btn(self, message: Message) -> None:
        """
        handle settings btn
        """
        self.bot.send_message(message.chat.id, 'Ваши текущие настройки',
                              reply_markup=self.keybords.settings_menu())

    def change_lesson(self, message: Message) -> None:
        """
        """
        list_of_records = self.BD.select_all_lessons()
        self.bot.send_message(message.chat.id, 'Какую запись обновить?',
                            reply_markup=self.keybords.set_list_of_lesson_for_upd_lesson(list_of_records))

    def show_admin_students_menu(self, message: Message) -> None:
        self.bot.send_message(message.chat.id, 'Записи со студентами',
                            reply_markup=self.keybords.set_students_action_menu())

    def pressed_new_student_btn(self, message: Message) -> None:
        self.bot.send_message(message.chat.id, 'Записи со студентами',
                            reply_markup=self.keybords.set_guests_inline_menu())


    def handle(self) -> None:

        @self.bot.message_handler(func=lambda message: True)
        def handle(message: Message) -> None:
            # ---- menu btns -----
            # admin keyboard btns
            if message.text == KEYBOARD['LESSONS']:
                self.show_admin_lessons_menu(message)

            if message.text == KEYBOARD['ALL_LESSONS']:
                self.show_all_lessons(message)

            if message.text == KEYBOARD['ADD_LESSON']:
                self.add_new_lesson(message)

            if message.text == KEYBOARD['CHANGE_LESSON']:
                self.change_lesson(message)

            if message.text == KEYBOARD['STUDENTS']:
                self.show_admin_students_menu(message)

            if message.text == KEYBOARD['GUESTS']:
                self.pressed_new_student_btn(message)

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
                self.pressed_settings_btn(message)

            if message.text == KEYBOARD['HELP']:
                self.pressed_help_btn(message)

            if message.text == KEYBOARD['RUS']:
                self.pressed_rus_lang_btn(message)

            if message.text == KEYBOARD['ENG']:
                self.pressed_eng_lang_btn(message)

            if message.text == KEYBOARD['<<']:
                self.pressed_back_btn(message)
