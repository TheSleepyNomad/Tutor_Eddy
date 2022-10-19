from handlers.handler import Handler


class HandlerInlineQuery(Handler):

    def __init__(self, bot):
        super().__init__(bot)

    def test(self, call):
        self.bot.send_message(call.id,'хочет прийти на пробное занятие.')

    def handle(self):
        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            print(call.data)
            print(call)
            self.test(call)
