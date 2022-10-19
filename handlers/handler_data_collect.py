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
        self.bot.send_message(ADMIN_ID,
                              f'{student.first_name} {student.last_name},'
                              'хочет прийти на пробное занятие. '
                              f'Вы можете связаться с ним по телефону {student.phone}',
                              reply_markup=self.keybords.guest_start_menu())

    def handle(self) -> None:
        @self.bot.message_handler(content_types=['contact'])
        def handle(message) -> None:
            self.save_user_phone(message)
            self.send_new_student_for_admin(message)
