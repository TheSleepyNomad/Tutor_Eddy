from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import NoResultFound
from database.database_core import Base
from models.students import Students
from config.settings import DATABASE
from os import path


class Singleton(type):

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class DBManager(metaclass=Singleton):

    def __init__(self) -> None:
        """
        run session and connect to the data base
        """
        self.engine = create_engine(DATABASE)
        session = sessionmaker(bind=self.engine)
        self._session = session()
        if not path.isfile(DATABASE):
            Base.metadata.create_all(self.engine)

    def close(self):
        """
        Close session
        """
        self._session.close()

    def check_user_on_exist_by_user_id(self, user_id) -> bool:
        try:
            result = self._session.query(
                Students).filter_by(user_id=user_id).one()
            self.close()
            return True

        except NoResultFound:
            self.close()
            return False

    def _add_new_student(self, username: str, user_id: str, first_name: str, last_name: str, phone=None) -> None:
        student = Students(username=username,
                           user_id=user_id,
                           first_name=first_name,
                           last_name=last_name,
                           phone=phone)

        self._session.add(student)
        self._session.commit()
        self.close()
