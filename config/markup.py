from telebot.types import KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from config.settings import KEYBOARD
from database.dbalchemy import DBManager
from utils.data_classes import LessonRecord
from datetime import timedelta, datetime


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

    def lesson_records(self, lesson_record: list) -> InlineKeyboardMarkup:
        # Todo переделать логику callback_data
        self.markup = InlineKeyboardMarkup(row_width=1)
        for itm in lesson_record:
            self.markup.add(InlineKeyboardButton(str(f'{itm.student_name} - {itm.lesson_name} - {itm.lesson_date}'),
                                                 callback_data=str({'lesson_record': itm.lesson_id})))

        return self.markup

    def students_start_menu(self) -> ReplyKeyboardMarkup:
        """
        set start menu for users with student role
        """
        self.markup = ReplyKeyboardMarkup(True)
        self.markup.add(self.set_btn('MY_LESSONS'))
        self.markup.add(self.set_btn('ABOUT_TUTOR'))
        self.markup.row(self.set_btn('HELP'), self.set_btn('SETTINGS'))
        return self.markup

    def admin_start_menu(self) -> ReplyKeyboardMarkup:
        """
        set start menu for users with admin role
        """
        self.markup = ReplyKeyboardMarkup(True)
        self.markup.add(self.set_btn('LESSONS'))
        self.markup.add(self.set_btn('STUDENTS'))
        self.markup.row(self.set_btn('HELP'), self.set_btn('SETTINGS'))
        return self.markup

    def guest_start_menu(self) -> ReplyKeyboardMarkup:
        """
        set start menu for users with guest role
        """
        self.markup = ReplyKeyboardMarkup(True)
        self.markup.add(self.set_btn('TEST_LESSON'))
        self.markup.row(self.set_btn('ABOUT_TUTOR'), self.set_btn('HELP'))
        self.markup.row(self.set_btn('SETTINGS'), self.set_btn('ABOUT_APP'))
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

    def settings_menu(self) -> ReplyKeyboardMarkup:
        """
        set setting menu for all users
        """
        self.markup = ReplyKeyboardMarkup(True)
        self.markup.row(self.set_btn('CHANGE_LNG'), self.set_btn('ABOUT_APP'))
        self.markup.add(self.set_btn('<<'))
        return self.markup

    def admin_lesson_records_menu(self) -> ReplyKeyboardMarkup:
        self.markup = ReplyKeyboardMarkup(True)
        self.markup.add(self.set_btn('ALL_LESSONS'))
        self.markup.row(self.set_btn('ADD_LESSON'),
                        self.set_btn('CHANGE_LESSON'))
        self.markup.add(self.set_btn('<<'))
        return self.markup

    def add_lesson_inline_btn(self) -> InlineKeyboardMarkup:
        """
        """
        self.markup = InlineKeyboardMarkup(row_width=1)
        for itm in self.BD.get_all_lesson_types():
            self.markup.add(InlineKeyboardButton(str(f'{itm.type_name}'),
                                                 callback_data=str({'add_lsn': itm.id})))

        return self.markup

    def add_lesson_student_inline_btn(self, lesson_id):
        self.markup = InlineKeyboardMarkup(row_width=1)
        for itm in self.BD.get_all_students():
            self.markup.add(InlineKeyboardButton(str(f'{itm.first_name}'),
                                                 callback_data=str({'add_lsn': itm.id, 'lsn_id': lesson_id})))

        return self.markup

    def add_lesson_student_date_inline_btn(self, lesson_id, student_id):
        date_list = [datetime.today() + timedelta(_) for _ in range(13)]
        self.markup = InlineKeyboardMarkup(row_width=1)
        for day in date_list:
            self.markup.add(InlineKeyboardButton(str(f'{day.date()}'),
                                                 callback_data=str({'add_lsn': student_id, 'lsn_id': lesson_id, 'date': str(day.date())})))
        return self.markup

    def update_lessons_menu(self, lesson_record):
        self.markup = InlineKeyboardMarkup(row_width=1)
        for itm in lesson_record:
            self.markup.add(InlineKeyboardButton(str(f'{itm.student_name} - {itm.lesson_name} - {itm.lesson_date}'),
                                                 callback_data=str({'upd_ls': itm.lesson_id})))

        return self.markup

    def upd_btns(self, lesson_id):
        self.markup = InlineKeyboardMarkup(row_width=1)
        self.markup.row(InlineKeyboardButton('Студента', callback_data=str(f'upd_ls user {lesson_id}')),
                        InlineKeyboardButton('Предмет', callback_data=str(
                            f'upd_ls ls_type {lesson_id}')),
                        InlineKeyboardButton('Дату', callback_data=str(f'upd_ls date {lesson_id}')))

        self.markup.add(InlineKeyboardButton('Статус оплаты',
                        callback_data=str(f'upd_ls pay {lesson_id}')))

        self.markup.add(InlineKeyboardButton(
            'Вернуться к списку', callback_data='return_to_upd_ls_list'))
        return self.markup

    def upd_student_btn(self, lesson_id):
        self.markup = InlineKeyboardMarkup(row_width=1)
        students = self.BD.get_all_students()
        for student in students:
            self.markup.add(InlineKeyboardButton(str(f'{student}'),
                                                 callback_data=f'upd_ls user value {lesson_id} {student.id}'))
        return self.markup

    def upd_ls_type_btn(self, lesson_id):
        self.markup = InlineKeyboardMarkup(row_width=1)
        lesson_types = self.BD.get_all_lesson_types()
        for lesson_type in lesson_types:
            self.markup.add(InlineKeyboardButton(str(f'{lesson_type}'),
                                                 callback_data=f'upd_ls ls_type value {lesson_id} {lesson_type.id}'))
        return self.markup

    def upd_ls_type_btn(self, lesson_id):
        self.markup = InlineKeyboardMarkup(row_width=1)
        lesson_types = self.BD.get_all_lesson_types()
        for lesson_type in lesson_types:
            self.markup.add(InlineKeyboardButton(str(f'{lesson_type}'),
                                                 callback_data=f'upd_ls ls_type value {lesson_id} {lesson_type.id}'))
        return self.markup

    def upd_date_btn(self, lesson_id):
        self.markup = InlineKeyboardMarkup(row_width=1)
        dates_list = [datetime.today() + timedelta(_) for _ in range(13)]
        for date_list in dates_list:
            self.markup.add(InlineKeyboardButton(str(f'{date_list}'),
                                                 callback_data=f'upd_ls date value {lesson_id} {date_list}'))
        return self.markup

    def upd_payment_btn(self, lesson_id):
        self.markup = InlineKeyboardMarkup(row_width=1)
        self.markup.row(InlineKeyboardButton('Да',
                        callback_data=f'upd_ls ls_type value {lesson_id} 1'),
                        InlineKeyboardButton('Нет',
                        callback_data=f'upd_ls ls_type value {lesson_id} 0'))

        return self.markup
