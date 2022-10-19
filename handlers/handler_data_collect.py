from handlers.handler import Handler


class HandlerDataCollect(Handler):

    def __init__(self, bot):
        super().__init__(bot)

    def handle(self) -> None:

        @self.bot.message_handler(content_types=['contact', 'location'])
        def handle(message) -> None:
            print(message.contact)
