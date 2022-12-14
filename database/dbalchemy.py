from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from database.database_core import Base
from models.students import Students
from models.lessons_type import LessonsType
from models.lessons import Lessons
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

    def check_user_on_exist_by_user_id(self, user_id: int) -> bool:
        try:
            result = self._session.query(
                Students).filter_by(user_id=user_id).one()
            self.close()
            return result

        except NoResultFound:
            self.close()
            return False

    def _add_new_student(self, username: str, user_id: str, first_name: str, last_name: str, phone=None, guest_is=True) -> None:
        student = Students(username=username,
                           user_id=user_id,
                           first_name=first_name,
                           last_name=last_name,
                           phone=phone,
                           guest_is=guest_is)

        self._session.add(student)
        self._session.commit()
        self.close()

    def update_student_profile(self, user_id: int, name: str, value) -> None:
        self._session.query(Students).filter_by(
            user_id=user_id).update({name: value})
        self._session.commit()
        self.close()

    def get_user_by_user_id(self, user_id: int):
        result = self._session.query(
            Students).filter_by(user_id=user_id).one()
        self.close()
        return result

    def get_guest_lesson_by_user_id(self, user_id: int):
        try:
            result = self._session.query(
                Lessons).filter_by(students_id=user_id, like_guest=True).one()
        except NoResultFound:
            self.close()
            return False
        self.close()
        return result

    def get_lesson_type_by_id(self, lesson_type_id: int):
        try:
            result = self._session.query(
                LessonsType).filter_by(id=lesson_type_id).one()
        except NoResultFound:
            self.close()
            return False
        except MultipleResultsFound:
            self.close()
            return False

        self.close()
        return result

    def get_all_lesson_types(self):
        result = self._session.query(LessonsType).all()
        self.close()
        return result

    def get_all_lesson_records(self):
        result = self._session.query(
            Lessons,
            LessonsType,
            Students).filter(
                Lessons.lessons_type_id == LessonsType.id
            ).filter(
                Lessons.students_id == Students.id
            ).all()
        self.close()
        return result

    def _add_new_lesson(self, student_id: int, lessons_type_id: int, guest: bool) -> None:
        lesson = Lessons(students_id=student_id, lessons_type_id=lessons_type_id,
                         like_guest=guest)
        self._session.add(lesson)
        self._session.commit()
        self.close()
