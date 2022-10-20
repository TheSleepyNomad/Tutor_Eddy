from cgitb import text
from re import I
from handlers.handler import Handler
from config.settings import KEYBOARD
from config.messages import MsgTemplates
from config.settings import ADMIN_ID
from telebot.types import CallbackQuery


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

    def handle(self):
        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call: CallbackQuery):
            data = call.data
            print(type(call))
            if data.isdigit():
                last_msg = self.record_on_test_lesson(call)
                self.del_last_bot_message(last_msg)

            else:
                self.more_about_lesson(call)
