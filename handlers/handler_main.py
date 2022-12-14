from handlers.handler_commands import HandlerCommands
from handlers.handler_all_text import HandlerAllText
from handlers.handler_data_collect import HandlerDataCollect
from handlers.handler_inline_query import HandlerInlineQuery
from telebot import TeleBot

class HandlerMain:

    def __init__(self, bot: TeleBot):
        self.bot = bot
        self.handler_commands = HandlerCommands(self.bot)
        self.handler_all_text = HandlerAllText(self.bot)
        self.handler_data_collect = HandlerDataCollect(self.bot)
        self.handler_inline_query = HandlerInlineQuery(self.bot)

    def handle(self) -> None:
        """
        run all handlers
        """
        self.handler_commands.handle()
        self.handler_all_text.handle()
        self.handler_data_collect.handle()
        self.handler_inline_query.handle()
