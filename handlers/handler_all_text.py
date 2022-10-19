from handlers.handler import Handler
from config.settings import KEYBOARD


class HandlerAllText(Handler):
    """
    Handle button from user keyboard
    """
    def __init__(self, bot):
        super().__init__(bot)




    def handle(self) -> None:

        @self.bot.message_handler(func=lambda message: True)
        def handle(message) -> None:
            # ---- menu btns -----
            # admin keyboard btns
            if message.text == KEYBOARD['LESSONS']:
                pass
            if message.text == KEYBOARD['ADD_STUDENT']:
                pass
            # student keyboard btns
            if message.text == KEYBOARD['MY_LESSONS']:
                pass
            # guest keyboard btns
            if message.text == KEYBOARD['TEST_LESSON']:
                pass
            # other btns
            if message.text == KEYBOARD['ABOUT_TUTOR']:
                pass
            if message.text == KEYBOARD['SETTINGS']:
                pass
            if message.text == KEYBOARD['REQ_PHONE']:
                pass
            if message.text == KEYBOARD['HELP']:
                pass
            if message.text == KEYBOARD['<<']:
                pass