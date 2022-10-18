import abc
from database.dbalchemy import DBManager
from config.markup import Keyboards

class Handler(metaclass=abc.ABCMeta):

    def __init__(self, bot):
        self.bot = bot
        self.keybords = Keyboards()
        self.BD = DBManager()

    @abc.abstractmethod
    def handle(self):
        pass
