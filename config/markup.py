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