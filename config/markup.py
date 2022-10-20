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

    def record_on_lesson_menu(self, lesson_type_id):
        self.markup = InlineKeyboardMarkup(row_width=1)
        self.markup.add(self.set_record_on_lesson_btn(lesson_type_id))
        return self.markup

    def set_record_on_lesson_btn(self, lesson_type_id):
        return InlineKeyboardButton(str('Записаться на пробное занятие'),
                                    callback_data=str(lesson_type_id))

    def set_inline_btn(self, name):
        return InlineKeyboardButton(str(name),
                                    callback_data=str(name.id))

    def set_lesson_inline_btn(self, lesson_type):
        return InlineKeyboardButton(str(lesson_type),
                                    callback_data=str(lesson_type.type_name))

    def guest_lesson_menu(self):
        self.markup = InlineKeyboardMarkup(row_width=1)
        
        for itm in self.BD.get_all_lesson_types():
            self.markup.add(self.set_lesson_inline_btn(itm))

        return self.markup

    def get_user_phone_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        self.markup.row(self.set_btn('REQ_PHONE', request_contact=True))
        self.markup.row(self.set_btn('<<'))
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
    # del in future
    def lessons_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        self.markup.add(self.set_btn('MATH'))
        self.markup.add(self.set_btn('ENGLISH'))
        self.markup.add(self.set_btn('SOCIAL'))
        return self.markup
    
    def choose_language_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        self.markup.row(self.set_btn('ENG'), self.set_btn('RUS'))
        return self.markup

    def get_user_phone(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        self.markup.add(self.set_btn('REQ_PHONE', True))
        return self.markup