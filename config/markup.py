from telebot.types import KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from config.settings import KEYBOARD
from database.dbalchemy import DBManager


class Keyboards:

    def __init__(self):
        self.markup = None
        self.BD = DBManager()

    def set_btn(self, name, request_contact=False) -> KeyboardButton:
        """
        set button on ReplyKeyboardMarkup
        """
        if request_contact:
            return KeyboardButton(KEYBOARD[name], request_contact=request_contact)

        return KeyboardButton(KEYBOARD[name])

    @staticmethod
    def remove_menu() -> ReplyKeyboardRemove:
        """
        delete markup
        """
        return ReplyKeyboardRemove()

    def record_on_lesson_menu(self, lesson_type_id: int) -> InlineKeyboardMarkup:
        """
        set inline btns, when user select record on lesson
        """
        self.markup = InlineKeyboardMarkup(row_width=1)
        self.markup.add(self.set_record_on_lesson_btn(lesson_type_id))
        return self.markup

    def set_record_on_lesson_btn(self, lesson_type_id: int) -> InlineKeyboardButton:
        """
        set inline btn for record new student on test lesson
        """
        return InlineKeyboardButton(str('Записаться на пробное занятие'),
                                    callback_data=str(lesson_type_id))

    def set_inline_btn(self, name) -> InlineKeyboardButton:
        """
        set inline btn
        """
        return InlineKeyboardButton(str(name), callback_data=str(name.id))

    def set_lesson_inline_btn(self, lesson_type):
        return InlineKeyboardButton(str(lesson_type),
                                    callback_data=str(lesson_type.type_name))

    def guest_lesson_menu(self) -> InlineKeyboardMarkup:
        """
        set inline menu with lessons name
        """
        self.markup = InlineKeyboardMarkup(row_width=1)
        for itm in self.BD.get_all_lesson_types():
            self.markup.add(self.set_lesson_inline_btn(itm))

        return self.markup

    def students_start_menu(self) -> ReplyKeyboardMarkup:
        """
        set start menu for users with student role
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        self.markup.add(self.set_btn('MY_LESSONS'))
        self.markup.add(self.set_btn('ABOUT_TUTOR'))
        return self.markup

    def admin_start_menu(self) -> ReplyKeyboardMarkup:
        """
        set start menu for users with admin role
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        self.markup.add(self.set_btn('LESSONS'))
        self.markup.add(self.set_btn('ADD_STUDENT'))
        self.markup.add(self.set_btn('SETTINGS'))
        return self.markup

    def guest_start_menu(self) -> ReplyKeyboardMarkup:
        """
        set start menu for users with guest role
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        self.markup.add(self.set_btn('TEST_LESSON'))
        self.markup.row(self.set_btn('ABOUT_TUTOR'), self.set_btn('ABOUT_APP'))
        self.markup.row(self.set_btn('SETTINGS'), self.set_btn('HELP'))
        return self.markup

    def choose_language_menu(self) -> ReplyKeyboardMarkup:
        """
        set choosing language menu btns
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        self.markup.row(self.set_btn('ENG'), self.set_btn('RUS'))
        return self.markup

    def get_user_phone(self) -> ReplyKeyboardMarkup:
        """
        set btn for getting user phone
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        self.markup.add(self.set_btn('REQ_PHONE', True))
        return self.markup
