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

    # Admin btns and keyboard
    def set_admin_lesson_action_menu(self) -> ReplyKeyboardMarkup:
        """
        Set menu, when admin pressed 'LESSON' btn
        """
        self.markup = ReplyKeyboardMarkup(True)
        self.markup.add(self.set_btn('ALL_LESSONS'))
        self.markup.row(self.set_btn('ADD_LESSON'),
                        self.set_btn('CHANGE_LESSON'))
        self.markup.add(self.set_btn('<<'))
        return self.markup

    def set_admin_menu(self) -> ReplyKeyboardMarkup:
        """
        set start menu for admin
        """
        self.markup = ReplyKeyboardMarkup(True)
        self.markup.add(self.set_btn('LESSONS'))
        self.markup.add(self.set_btn('STUDENTS'))
        self.markup.row(self.set_btn('HELP'), self.set_btn('SETTINGS'))
        return self.markup

    def set_lessons_inline_menu(self, lesson_record: list) -> InlineKeyboardMarkup:
        """
        Set list of lessons, when admin wanna see all lessons
        """
        self.markup = InlineKeyboardMarkup(row_width=1)
        for itm in lesson_record:
            self.markup.add(InlineKeyboardButton(str(f'{itm.student_name} - {itm.lesson_name} - {itm.lesson_date}'),
                                                 callback_data=str({'lesson_info': itm.lesson_id})))

        return self.markup

    def set_guests_inline_menu(self) -> InlineKeyboardMarkup:
        """
        Set list of lessons, when admin wanna see all lessons
        """
        self.markup = InlineKeyboardMarkup(row_width=1)
        guests = self.BD.select_all_guest()
        for guest in guests:
            self.markup.add(InlineKeyboardButton(str(f'{guest.first_name} - {guest.last_name} - {guest.phone}'),
                                                 callback_data=str({'edit_guest': guest.id})))

        return self.markup

    def set_all_student_inline_menu(self) -> InlineKeyboardMarkup:
        self.markup = InlineKeyboardMarkup(row_width=1)
        students = self.BD.select_all_students()
        for student in students:
            self.markup.add(InlineKeyboardButton(str(f'{student.first_name} - {student.last_name} - {student.phone}'),
                                                 callback_data=str({'student_info': student.id})))
        return self.markup

    # upd guest
    def set_guest_edit_menu(self, guest_id: int) -> InlineKeyboardMarkup:
        self.markup = InlineKeyboardMarkup(row_width=1)
        self.markup.add(InlineKeyboardButton('Добавить в студенты',
                                                 callback_data=str({'edit_guest': guest_id, 'guest_is': 0})))
        return self.markup

    def set_students_action_menu(self) -> ReplyKeyboardMarkup:
        """
        Set menu, when admin pressed 'STUDENTS' btn
        """
        self.markup = ReplyKeyboardMarkup(True)
        self.markup.add(self.set_btn('ALL_STUDENTS'))
        self.markup.add(self.set_btn('GUESTS'))
        self.markup.add(self.set_btn('<<'))
        return self.markup

    # add lesson
    def set_list_of_lessons_for_add_lesson(self) -> InlineKeyboardMarkup:
        """
        Set list of lessons for add
        """
        self.markup = InlineKeyboardMarkup(row_width=1)
        for itm in self.BD.select_all_lesson_types():
            self.markup.add(InlineKeyboardButton(str(f'{itm.type_name}'),
                                                 callback_data=str({'add_lsn': itm.id})))

        return self.markup

    def set_list_of_students_for_add_lesson(self, lesson_id):
        """
        Set list of students for add
        """
        self.markup = InlineKeyboardMarkup(row_width=1)
        for itm in self.BD.select_all_students():
            self.markup.add(InlineKeyboardButton(str(f'{itm.first_name}'),
                                                 callback_data=str({'add_lsn': itm.id, 'lsn_id': lesson_id})))

        return self.markup

    def set_list_of_dates_for_add_leeson(self, lesson_id, student_id):
        """
        Set list of dates for add
        """
        date_list = [datetime.today() + timedelta(_) for _ in range(13)]
        self.markup = InlineKeyboardMarkup(row_width=1)
        for day in date_list:
            self.markup.add(InlineKeyboardButton(str(f'{day.date()}'),
                                                 callback_data=str({'add_lsn': student_id, 'lsn_id': lesson_id, 'date': str(day.date())})))
        return self.markup

    # update lesson
    def set_list_of_lesson_for_upd_lesson(self, lesson_record):
        """
        Set list of lessons for upd
        """
        self.markup = InlineKeyboardMarkup(row_width=1)
        for itm in lesson_record:
            self.markup.add(InlineKeyboardButton(str(f'{itm.student_name} - {itm.lesson_name} - {itm.lesson_date}'),
                                                 callback_data=str({'upd_ls': itm.lesson_id})))

        return self.markup

    def set_btns_for_upd_lesson(self, lesson_id):
        """
        Set btns for upd
        """
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

    def set_list_of_students_for_upd_lesson(self, lesson_id):
        """
        Set list of students for upd
        """
        self.markup = InlineKeyboardMarkup(row_width=1)
        students = self.BD.select_all_students()
        for student in students:
            self.markup.add(InlineKeyboardButton(str(f'{student}'),
                                                 callback_data=f'upd_ls user value {lesson_id} {student.id}'))
        return self.markup

    def set_list_of_lesson_type_for_upd_lesson(self, lesson_id):
        """
        Set list of lesson_types for upd
        """
        self.markup = InlineKeyboardMarkup(row_width=1)
        lesson_types = self.BD.select_all_lesson_types()
        for lesson_type in lesson_types:
            self.markup.add(InlineKeyboardButton(str(f'{lesson_type}'),
                                                 callback_data=f'upd_ls ls_type value {lesson_id} {lesson_type.id}'))
        return self.markup

    def set_list_of_date_for_upd_lesson(self, lesson_id):
        """
        Set list of dates for upd
        """
        self.markup = InlineKeyboardMarkup(row_width=1)
        dates_list = [datetime.today() + timedelta(_) for _ in range(13)]
        for date_list in dates_list:
            self.markup.add(InlineKeyboardButton(str(f'{date_list}'),
                                                 callback_data=f'upd_ls date value {lesson_id} {date_list}'))
        return self.markup

    def set_list_of_pay_btns_for_upd_lesson(self, lesson_id):
        """
        Set list of pay btn for upd
        """
        self.markup = InlineKeyboardMarkup(row_width=1)
        self.markup.row(InlineKeyboardButton('Да',
                        callback_data=f'upd_ls ls_type value {lesson_id} 1'),
                        InlineKeyboardButton('Нет',
                        callback_data=f'upd_ls ls_type value {lesson_id} 0'))

        return self.markup

    # Students btns and keyboard
    def set_students_menu(self) -> ReplyKeyboardMarkup:
        """
        set start menu for users with student role
        """
        self.markup = ReplyKeyboardMarkup(True)
        self.markup.add(self.set_btn('MY_LESSONS'))
        self.markup.add(self.set_btn('ABOUT_TUTOR'))
        self.markup.row(self.set_btn('HELP'), self.set_btn('SETTINGS'))
        return self.markup

    # Guest btns and keyboard
    def set_guest_menu(self) -> ReplyKeyboardMarkup:
        """
        set start menu for users with guest role
        """
        self.markup = ReplyKeyboardMarkup(True)
        self.markup.add(self.set_btn('TEST_LESSON'))
        self.markup.row(self.set_btn('ABOUT_TUTOR'), self.set_btn('HELP'))
        self.markup.row(self.set_btn('SETTINGS'), self.set_btn('ABOUT_APP'))
        return self.markup

    def set_sign_up_btn(self, lesson_type_id: int) -> InlineKeyboardMarkup:
        """
        set inline btns, when user select record on lesson
        """
        self.markup = InlineKeyboardMarkup(row_width=1)
        self.markup.add(InlineKeyboardButton(str('Записаться на пробное занятие'),
                                             callback_data=str(lesson_type_id)))
        return self.markup

    def set_guest_menu(self) -> InlineKeyboardMarkup:
        """
        set inline menu with lessons name
        """
        self.markup = InlineKeyboardMarkup(row_width=1)
        for itm in self.BD.select_all_lesson_types():
            self.markup.add(InlineKeyboardButton(str(itm),
                                                 callback_data=str(itm.type_name)))

        return self.markup

    # Other functions
    def language_selection_menu(self) -> ReplyKeyboardMarkup:
        """
        set choosing language menu btns
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        self.markup.row(self.set_btn('ENG'), self.set_btn('RUS'))
        return self.markup

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

    def set_request_phone_menu(self) -> ReplyKeyboardMarkup:
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

    def set_inline_btn(self, name) -> InlineKeyboardButton:
        """
        set inline btn
        """
        return InlineKeyboardButton(str(name), callback_data=str(name.id))
    # -------------------------------------
