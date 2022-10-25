
from datetime import datetime
from handlers.handler import Handler
from config.settings import KEYBOARD
from config.messages import MsgTemplates
from config.settings import ADMIN_ID
from telebot.types import CallbackQuery
from re import findall, match


class HandlerInlineQuery(Handler):

    def __init__(self, bot):
        super().__init__(bot)

    def send_new_student_for_admin(self, user):
        """
        send notification about new student for admin
        """
        student_lesson = self.BD.get_guest_lesson_by_user_id(user.id)
        lesson_type = self.BD.get_lesson_type_by_id(
            student_lesson.lessons_type_id)
        self.bot.send_message(ADMIN_ID,
                              f'{user.first_name} {user.last_name}, '
                              f'хочет прийти на пробное занятие по {lesson_type}. '
                              f'Вы можете связаться с ним по телефону {user.phone}',
                              reply_markup=self.keybords.guest_start_menu())

    def record_on_test_lesson(self, call: CallbackQuery) -> CallbackQuery:
        """
        write user on test lesson
        """
        guest = self.BD.get_user_by_user_id(call.from_user.id)
        last_msg = call.message
        self.BD._add_new_lesson(guest.id, call.data, True)
        self.send_new_student_for_admin(guest)
        self.bot.answer_callback_query(
            call.id, 'Вы записаны - ждите', show_alert=True)
        return last_msg

    def del_last_bot_message(self, message) -> None:
        """
        delete inline btn
        """
        self.bot.edit_message_text(
            chat_id=message.chat.id, text=message.text, message_id=message.id, reply_markup='')

    def more_about_lesson(self, call: CallbackQuery) -> None:
        """
        show extendent information about lessons
        """
        self.bot.answer_callback_query(call.id)

        user = self.BD.get_user_by_user_id(call.from_user.id)
        lesson = self.BD.get_guest_lesson_by_user_id(user.id)

        if call.data == 'Математика':
            if lesson:
                self.bot.send_message(
                    call.from_user.id, MsgTemplates.ABOUT_MATH_MSG)
            else:
                self.bot.send_message(call.from_user.id, MsgTemplates.ABOUT_MATH_MSG,
                                      reply_markup=self.keybords.record_on_lesson_menu(1))

        if call.data == 'Английский язык':
            if lesson:
                self.bot.send_message(
                    call.from_user.id, MsgTemplates.ABOUT_ENG_MSG)
            else:
                self.bot.send_message(call.from_user.id, MsgTemplates.ABOUT_ENG_MSG,
                                      reply_markup=self.keybords.record_on_lesson_menu(2))

        if call.data == 'Обществознание':
            if lesson:
                self.bot.send_message(
                    call.from_user.id, MsgTemplates.ABOUT_SOCIAL_MSG)
            else:
                self.bot.send_message(call.from_user.id, MsgTemplates.ABOUT_SOCIAL_MSG,
                                      reply_markup=self.keybords.record_on_lesson_menu(3))

    def show_extended_info(self, call: CallbackQuery) -> None:
        lesson_record = self.BD.get_one_lesson_records(
            int(call.data[17:-1].strip()))
        print(lesson_record)
        self.bot.answer_callback_query(call.id, MsgTemplates.ABOUT_LESSON_MSG.format(
            lesson_record[0].student_name,
            lesson_record[0].student_phone,
            lesson_record[0].lesson_name,
            lesson_record[0].lesson_date,
            lesson_record[0].is_payment),
            show_alert=True)

    def add_lesson_select_student(self, call, lesson_name):
        self.bot.answer_callback_query(call.id)
        self.bot.edit_message_text(
            chat_id=call.message.chat.id, text=f'Кого записываем на {lesson_name.type_name}', message_id=call.message.id, reply_markup=self.keybords.add_lesson_student_inline_btn(lesson_name.id))

    def add_lesson_select_date(self, call, lesson_id, student_id):
        self.bot.answer_callback_query(call.id)
        self.bot.edit_message_text(
            chat_id=call.message.chat.id, text=f'На какое число записать?', message_id=call.message.id, reply_markup=self.keybords.add_lesson_student_date_inline_btn(lesson_id, student_id))

    def create_new_lesson_record(self, call, lesson_id, student_id, date):
        self.bot.answer_callback_query(call.id)
        self.BD._add_new_lesson(student_id, lesson_id,
                                False, datetime.strptime(date, '%Y-%m-%d'))

    def selected_lesson(self, call):
        self.bot.answer_callback_query(call.id)
        lesson_id = findall('\d+', call.data)
        self.bot.edit_message_text(
            chat_id=call.message.chat.id, text=f'Что вы хотите изменить?', message_id=call.message.id, reply_markup=self.keybords.upd_btns(lesson_id))

    def select_for_upd_student(self, call):
        self.bot.answer_callback_query(call.id)
        lesson_id = findall('\d+', call.data)
        self.bot.edit_message_text(
            chat_id=call.message.chat.id, text=f'Какого студента добавить?', message_id=call.message.id, reply_markup=self.keybords.upd_student_btn(lesson_id))

    def select_for_upd_ls_type(self, call):
        self.bot.answer_callback_query(call.id)
        lesson_id = findall('\d+', call.data)
        self.bot.edit_message_text(
            chat_id=call.message.chat.id, text=f'Изменить предмет', message_id=call.message.id, reply_markup=self.keybords.upd_ls_type_btn(lesson_id))

    def select_for_upd_date(self, call):
        self.bot.answer_callback_query(call.id)
        lesson_id = findall('\d+', call.data)
        self.bot.edit_message_text(
            chat_id=call.message.chat.id, text=f'На какую дату перенести', message_id=call.message.id, reply_markup=self.keybords.upd_date_btn(lesson_id))

    def select_for_upd_pay(self, call):
        self.bot.answer_callback_query(call.id)
        lesson_id = findall('\d+', call.data)
        self.bot.edit_message_text(
            chat_id=call.message.chat.id, text=f'Оплата была?', message_id=call.message.id, reply_markup=self.keybords.upd_payment_btn(lesson_id))
        
    def upd_lesson_record(self, call, student_id=None, lesson_type_id=None, date=None, payment=None):
        self.bot.answer_callback_query(call.id)
        if student_id:
            print('----')
            lesson_id, value = findall('\d+', call.data)
            self.BD.update_lesson(lesson_id, student_id, value)

        elif lesson_type_id:
            lesson_id, value = findall('\d+', call.data)
            self.BD.update_lesson(lesson_id, lesson_type_id, value)
            
        elif date:
            lesson_id = findall('\d+', call.data)
            value = findall('\d+.\d+.\d+', call.data)
            self.BD.update_lesson(lesson_id[0], date, datetime.strptime(value[0], '%Y-%m-%d'))
        elif payment:
            lesson_id, value = findall('\d+', call.data)
            self.BD.update_lesson(lesson_id, payment, True)
        
        self.bot.edit_message_text(
            chat_id=call.message.chat.id, text=f'Успешно!', message_id=call.message.id, reply_markup='')

    def handle(self):
        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call: CallbackQuery):
            data = call.data
            if 'lesson_record' in data:
                self.show_extended_info(call)

            if 'add_lsn' in data:

                if 'lsn_id' in data:

                    if 'date' in data:
                        date = findall('\d+.\d+.\d+', data)
                        re_data = findall('\d+', data)
                        lesson_id, student_id = re_data[0:2]
                        print(date, lesson_id, student_id)
                        self.create_new_lesson_record(
                            call, lesson_id, student_id, date[0])
                    else:
                        student_id, lesson_id = findall('\d+', data)
                        self.add_lesson_select_date(
                            call, student_id, lesson_id)

                else:
                    lesson_id = findall('\d+', data)
                    lesson_name = self.BD.get_lesson_type_by_id(
                        int(lesson_id[0]))
                    self.add_lesson_select_student(call, lesson_name)
                    # print(call.id)

            if 'upd_ls' in data:
                if 'user' in data:
                    if 'value' in data:
                        self.upd_lesson_record(call, student_id='students_id')
                    else:
                        self.select_for_upd_student(call)
                elif 'ls_type' in data:
                    if 'value' in data:
                        self.upd_lesson_record(call, lesson_type_id='lessons_type_id')
                    else:
                        self.select_for_upd_ls_type(call)
                elif 'date' in data:
                    if 'value' in data:
                        self.upd_lesson_record(call, date='date')
                    else:
                        self.select_for_upd_date(call)
                elif 'pay' in data:
                    if 'value' in data:
                        self.upd_lesson_record(call, payment='payment')
                    else:
                        self.select_for_upd_pay(call)
                else:
                    self.selected_lesson(call)

            if 'select_student' in data:
                print(call.data)

            if data.isdigit():
                last_msg = self.record_on_test_lesson(call)
                self.del_last_bot_message(last_msg)

            else:
                self.more_about_lesson(call)
