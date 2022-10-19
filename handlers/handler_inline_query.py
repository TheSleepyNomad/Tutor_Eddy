from handlers.handler import Handler


class HandlerInlineQuery(Handler):

    def __init__(self, bot):
        super().__init__(bot)


    def test(self, call):
        self.bot.answer_callback_query(call.id, 'Тревога', show_alert=True)
    
    def handle(self):
        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            print(call.data)
            print(call)
            self.test(call)
            