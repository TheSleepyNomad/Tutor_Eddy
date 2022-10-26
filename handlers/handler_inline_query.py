
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

    def send_notification_about_new_student(self, user):
        """
        send notification about new student for admin
        """
        # get lesson record
        lesson = self.BD.select_one_lesson_filter_by_guest(user.id)
        # get lesson name
        lesson_type = self.BD.select_one_lesson_type(
            lesson.lessons_type_id)
        # send notification for admin
        self.bot.send_message(ADMIN_ID,
                              f'{user.first_name} {user.last_name}, '
                              f'хочет прийти на пробное занятие по {lesson_type}. '
                              f'Вы можете связаться с ним по телефону {user.phone}',
                              reply_markup=self.keybords.set_guest_menu())

    # Todo raname this function
    def record_on_test_lesson(self, call: CallbackQuery) -> CallbackQuery:
        """
        write user on test lesson
        """
        guest = self.BD.select_one_student_by_id(call.from_user.id)
        last_msg = call.message
        self.BD._add_new_lesson(guest.id, call.data, True)
        self.send_notification_about_new_student(guest)
        self.bot.answer_callback_query(
            call.id, 'Вы записаны - ждите', show_alert=True)
        return last_msg

    def delete_last_bot_message(self, message) -> None:
        """
        delete inline btn
        """
        self.bot.edit_message_text(
            chat_id=message.chat.id, text=message.text, message_id=message.id, reply_markup='')

    def show_extended_lesson_info_for_user(self, call: CallbackQuery) -> None:
        """
        show extendent information about lessons
        """
        self.bot.answer_callback_query(call.id)

        # get user by telegram id
        user = self.BD.select_one_student_by_id(call.from_user.id)

        # check lesson on exist
        lesson = self.BD.select_one_lesson_filter_by_guest(user.id)

        # if lesson not exist - send btn for recording
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

    def show_extended_lesson_info_for_admin(self, call: CallbackQuery) -> None:
        lesson_record = self.BD.select_one_lesson(
            int(call.data[17:-1].strip()))
        self.bot.answer_callback_query(call.id, MsgTemplates.ABOUT_LESSON_MSG.format(
            lesson_record[0].student_name,
            lesson_record[0].student_phone,
            lesson_record[0].lesson_name,
            lesson_record[0].lesson_date,
            lesson_record[0].is_payment),
            show_alert=True)

    # add new lesson
    def select_student_for_new_lesson(self, call, lesson_name):
        self.bot.answer_callback_query(call.id)
        self.bot.edit_message_text(
            chat_id=call.message.chat.id, text=f'Кого записываем на {lesson_name.type_name}', message_id=call.message.id, reply_markup=self.keybords.set_list_of_students_for_add_lesson(lesson_name.id))

    def select_date_for_new_lesson(self, call, lesson_id, student_id):
        self.bot.answer_callback_query(call.id)
        self.bot.edit_message_text(
            chat_id=call.message.chat.id, text=f'На какое число записать?', message_id=call.message.id, reply_markup=self.keybords.set_list_of_dates_for_add_leeson(lesson_id, student_id))

    def create_new_lesson(self, call, lesson_id, student_id, date):
        self.bot.answer_callback_query(call.id)
        self.BD._add_new_lesson(student_id, lesson_id,
                                False, datetime.strptime(date, '%Y-%m-%d'))

    # update lesson
    def select_lesson_for_upd(self, call):
        self.bot.answer_callback_query(call.id)
        lesson_id = findall('\d+', call.data)
        self.bot.edit_message_text(
            chat_id=call.message.chat.id, text=f'Что вы хотите изменить?', message_id=call.message.id, reply_markup=self.keybords.set_btns_for_upd_lesson(lesson_id))

    def select_student_for_lesson_upd(self, call):
        self.bot.answer_callback_query(call.id)
        lesson_id = findall('\d+', call.data)
        self.bot.edit_message_text(
            chat_id=call.message.chat.id, text=f'Какого студента добавить?', message_id=call.message.id, reply_markup=self.keybords.set_list_of_lesson_for_upd_lesson(lesson_id))

    def select_lesson_type_for_upd_lesson(self, call):
        self.bot.answer_callback_query(call.id)
        lesson_id = findall('\d+', call.data)
        self.bot.edit_message_text(
            chat_id=call.message.chat.id, text=f'Изменить предмет', message_id=call.message.id, reply_markup=self.keybords.set_list_of_lesson_type_for_upd_lesson(lesson_id))

    def select_date_for_upd_lesson(self, call):
        self.bot.answer_callback_query(call.id)
        lesson_id = findall('\d+', call.data)
        self.bot.edit_message_text(
            chat_id=call.message.chat.id, text=f'На какую дату перенести', message_id=call.message.id, reply_markup=self.keybords.set_list_of_date_for_upd_lesson(lesson_id))

    def select_pay_for_upd_lesson(self, call):
        self.bot.answer_callback_query(call.id)
        lesson_id = findall('\d+', call.data)
        self.bot.edit_message_text(
            chat_id=call.message.chat.id, text=f'Оплата была?', message_id=call.message.id, reply_markup=self.keybords.set_list_of_pay_btns_for_upd_lesson(lesson_id))

    # Todo think about refactorin/ find how optimizate
    def upd_selected_lesson(self, call, student_id=None, lesson_type_id=None, date=None, payment=None):
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
            self.BD.update_lesson(
                lesson_id[0], date, datetime.strptime(value[0], '%Y-%m-%d'))
        elif payment:
            lesson_id, value = findall('\d+', call.data)
            self.BD.update_lesson(lesson_id, payment, True)

        self.bot.edit_message_text(
            chat_id=call.message.chat.id, text=f'Успешно!', message_id=call.message.id, reply_markup='')

    def handle(self):
        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call: CallbackQuery):

            data = call.data
            # if admin wanna know lesson details
            # aka student name/phone/payed and other
            if 'lesson_info' in data:
                self.show_extended_lesson_info_for_admin(call)

            # if admin wanna create new lesson
            # this block handle inline menu
            # 1. bot send list of lesson_type
            # 2. bot edit old msg and send list of students
            # 3. finally bot last time edit msg and send inline list of dates
            if 'add_lsn' in data:
                # if admin select student - go deep
                if 'lsn_id' in data:
                    # if admin select date - go deep
                    if 'date' in data:
                        date = findall('\d+.\d+.\d+', data)
                        re_data = findall('\d+', data)
                        lesson_id, student_id = re_data[0:2]
                        print(date, lesson_id, student_id)
                        self.create_new_lesson(
                            call, lesson_id, student_id, date[0])
                    # if admin dont select date - show dates (14 days) inline list
                    else:
                        student_id, lesson_id = findall('\d+', data)
                        self.select_date_for_new_lesson(
                            call, student_id, lesson_id)
                # if admin dont select student - show students inline list
                else:
                    lesson_id = findall('\d+', data)
                    lesson_name = self.BD.select_one_lesson_type(
                        int(lesson_id[0]))
                    self.select_student_for_new_lesson(call, lesson_name)
                    # print(call.id)

            # if admin wanna upd lesson
            # 1. bot send list of lessons
            # 2. user select inline record
            # 3. bot edit msg and send btns for editing
            # 4. Depending on what the user has chosen - send inline list of students/date and other
            # if admin select lesson for up
            if 'upd_ls' in data:
                # if admin wanna change student in lesson
                if 'user' in data:
                    # if admin selected student
                    if 'value' in data:
                        self.upd_selected_lesson(call,
                                                 student_id='students_id')
                    else:
                        self.select_student_for_lesson_upd(call)
                # if admin wanna change lessontype in lesson
                elif 'ls_type' in data:
                    # if admin selected lesson type
                    if 'value' in data:
                        self.upd_selected_lesson(call,
                                                 lesson_type_id='lessons_type_id')
                    else:
                        self.select_lesson_type_for_upd_lesson(call)
                # if admin wanna change date in lesson
                elif 'date' in data:
                    # if admin selected date
                    if 'value' in data:
                        self.upd_selected_lesson(call, date='date')
                    else:
                        self.select_date_for_upd_lesson(call)
                # if admin wanna change payment status in lesson
                elif 'pay' in data:
                    # if admin selected payment status
                    if 'value' in data:
                        self.upd_selected_lesson(call, payment='payment')
                    else:
                        self.select_pay_for_upd_lesson(call)
                else:
                    self.select_lesson_for_upd(call)

            # this check use when guest already recording on lesson
            if data.isdigit():
                last_msg = self.record_on_test_lesson(call)
                self.delete_last_bot_message(last_msg)
            else:
                self.show_extended_lesson_info_for_user(call)
