from handlers.handler import Handler
from config.settings import KEYBOARD


class HandlerInlineQuery(Handler):

    def __init__(self, bot):
        super().__init__(bot)

    def test(self, call):
        self.bot.answer_callback_query(call.id)
        guest = self.BD.get_user_by_user_id(call.from_user.id)
        print(guest.id)
        self.BD._add_new_lesson(guest.id, 1, True)
        self.bot.send_message(call.from_user.id, KEYBOARD['MATH'],
                              reply_markup=self.keybords.get_user_phone_menu())

    def handle(self):
        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            print(call.data)
            print(call)
            self.test(call)
