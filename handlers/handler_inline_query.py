from cgitb import text
from handlers.handler import Handler
from config.settings import KEYBOARD
from config.messages import MsgTemplates
from config.settings import ADMIN_ID


class HandlerInlineQuery(Handler):

    def __init__(self, bot):
        super().__init__(bot)

    def send_new_student_for_admin(self, user):
        student_lesson = self.BD.get_guest_lesson_by_user_id(user.id)
        lesson_type = self.BD.get_lesson_type_by_id(
            student_lesson.lessons_type_id)
        self.bot.send_message(ADMIN_ID,
                              f'{user.first_name} {user.last_name}, '
                              f'хочет прийти на пробное занятие по {lesson_type}. '
                              f'Вы можете связаться с ним по телефону {user.phone}',
                              reply_markup=self.keybords.guest_start_menu())

    def record_on_test_lesson(self, call):
        guest = self.BD.get_user_by_user_id(call.from_user.id)
        last_msg = call.message
        print(call.message.chat.id)
        self.BD._add_new_lesson(guest.id, call.data, True)
        self.send_new_student_for_admin(guest)
        self.bot.answer_callback_query(call.id, 'Вы записаны - ждите', show_alert=True)

        return last_msg

    def del_last_bot_message(self, message):
        self.bot.edit_message_text(chat_id=message.chat.id, text=message.text, message_id=message.id, reply_markup='')

    def more_about_math(self, call):
        self.bot.answer_callback_query(call.id)
        self.bot.send_message(call.from_user.id, MsgTemplates.ABOUT_MATH_MSG,
                              reply_markup=self.keybords.record_on_lesson_menu(1))

    def more_about_english(self, call):
        self.bot.answer_callback_query(call.id)
        self.bot.send_message(call.from_user.id, MsgTemplates.ABOUT_ENG_MSG,
                              reply_markup=self.keybords.record_on_lesson_menu(2))

    def more_about_social(self, call):
        self.bot.answer_callback_query(call.id)
        self.bot.send_message(call.from_user.id, MsgTemplates.ABOUT_SOCIAL_MSG,
                              reply_markup=self.keybords.record_on_lesson_menu(3))

    def handle(self):
        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            data = call.data

            if data.isdigit():
                last_msg = self.record_on_test_lesson(call)
                self.del_last_bot_message(last_msg)
            
            if data == 'Математика':
                self.more_about_math(call)

            if data == 'Английский язык':
                self.more_about_english(call)

            if data == 'Обществознание':
                self.more_about_social(call)