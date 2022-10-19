from handlers.handler import Handler
from config.settings import KEYBOARD
from config.messages import MsgTemplates


class HandlerAllText(Handler):
    """
    Handle button from user keyboard
    """
    def __init__(self, bot):
        super().__init__(bot)

    def pressed_help_btn(self, message) -> None:
        self.bot.send_message(message.chat.id,
                                  f'{MsgTemplates.HELP_MSG}')

    def pressed_about_app_btn(self, message) -> None:
        self.bot.send_message(message.chat.id,
                                  f'{MsgTemplates.ABOUT_APP_MSG}')

    def pressed_about_tutor_btn(self, message) -> None:
        self.bot.send_message(message.chat.id,
                                  f'{MsgTemplates.ABOUT_TUTOR_MSG}')



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
                self.pressed_about_tutor_btn(message)

            if message.text == KEYBOARD['ABOUT_APP']:
                self.pressed_about_app_btn(message)

            if message.text == KEYBOARD['SETTINGS']:
                pass

            if message.text == KEYBOARD['REQ_PHONE']:
                pass

            if message.text == KEYBOARD['HELP']:
                self.pressed_help_btn(message)
                
            if message.text == KEYBOARD['<<']:
                pass