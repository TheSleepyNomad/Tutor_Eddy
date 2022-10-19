from telebot.types import KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from config.settings import KEYBOARD
from database.dbalchemy import DBManager


class Keyboards:

    def __init__(self):
        self.markup = None
        self.BD = DBManager()

    def set_btn(self, name, request_contact=False):
        if request_contact:
            return KeyboardButton(KEYBOARD[name], request_contact=request_contact)
        return KeyboardButton(KEYBOARD[name])

    @staticmethod
    def remove_menu():
        return ReplyKeyboardRemove()

    @staticmethod
    def set_inline_btn(name):
        return InlineKeyboardButton(str(name),
                                    callback_data=str(name.id))

    def get_user_phone_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        self.markup.row(self.set_btn('REQ_PHONE', request_contact=True))
        return self.markup

    def students_start_menu(self) -> ReplyKeyboardMarkup:
        self.markup = ReplyKeyboardMarkup(True, True)
        self.markup.add(self.set_btn('MY_LESSONS'))
        self.markup.add(self.set_btn('ABOUT_TUTOR'))
        self.markup.row(self.set_btn('SETTINGS'), self.set_btn('ABOUT_APP'))
        return self.markup

    def admin_start_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        self.markup.add(self.set_btn('LESSONS'))
        self.markup.add(self.set_btn('ADD_STUDENT'))
        self.markup.add(self.set_btn('SETTINGS'))
        return self.markup

    def guest_start_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        self.markup.add(self.set_btn('TEST_LESSON'))
        self.markup.add(self.set_btn('HELP'))
        self.markup.add(self.set_btn('ABOUT_TUTOR'))
        self.markup.add(self.set_btn('ABOUT_APP'))
        return self.markup

    def lessons_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        self.markup.add(self.set_btn('MATH'))
        self.markup.add(self.set_btn('ENG'))
        self.markup.add(self.set_btn('SOCIAL'))
        return self.markup
