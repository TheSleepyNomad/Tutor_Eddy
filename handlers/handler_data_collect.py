from handlers.handler import Handler
from config.settings import ADMIN_ID
from config.messages import MsgTemplates
from telebot.types import Message


class HandlerDataCollect(Handler):

    def __init__(self, bot):
        super().__init__(bot)

    def save_user_phone(self, message: Message) -> None:
        self.BD._add_new_student(message.from_user.username,
                                 message.from_user.id,
                                 message.from_user.first_name,
                                 message.from_user.last_name,
                                 phone=message.contact.phone_number)

        self.bot.send_message(message.chat.id,
                              f'{MsgTemplates.GUEST_START_MSG}',
                              reply_markup=self.keybords.set_guest_menu())

    def handle(self) -> None:
        @self.bot.message_handler(content_types=['contact'])
        def handle(message: Message) -> None:
            self.save_user_phone(message)
