from handlers.handler import Handler
from config.settings import ADMIN_ID


class HandlerDataCollect(Handler):

    def __init__(self, bot):
        super().__init__(bot)

    def save_user_phone(self, message) -> None:
        self.BD.update_student_profile(user_id=message.contact.user_id,
                                       name='phone',
                                       value=message.contact.phone_number)

    def send_new_student_for_admin(self, message):
        student = self.BD.get_user_by_user_id(user_id=message.contact.user_id)
        student_lesson = self.BD.get_guest_lesson_by_user_id(student.id)
        lesson_type = self.BD.get_lesson_type_by_id(student_lesson.lessons_type_id)
        print(lesson_type)
        self.bot.send_message(ADMIN_ID,
                              f'{student.first_name} {student.last_name}, '
                              f'хочет прийти на пробное занятие по {lesson_type}. '
                              f'Вы можете связаться с ним по телефону {student.phone}',
                              reply_markup=self.keybords.guest_start_menu())

    def handle(self) -> None:
        @self.bot.message_handler(content_types=['contact'])
        def handle(message) -> None:
            self.save_user_phone(message)
            self.send_new_student_for_admin(message)
