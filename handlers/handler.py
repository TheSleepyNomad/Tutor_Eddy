import abc
from database.dbalchemy import DBManager


class Handler(metaclass=abc.ABCMeta):

    def __init__(self, bot):
        self.bot = bot
        self.BD = DBManager()

    @abc.abstractmethod
    def handle(self):
        pass
