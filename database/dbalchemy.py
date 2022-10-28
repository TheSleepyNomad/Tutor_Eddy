from typing import Union
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from database.database_core import Base
from models.students import Students
from models.lessons_type import LessonsType
from models.lessons import Lessons
from config.settings import DATABASE, ADMIN_ID
from os import path
from utils.utils import _convert_in_class
from datetime import date, datetime


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

    # Lesson table
    def _add_new_lesson(self, student_id: int, lessons_type_id: int, guest: bool, date=datetime.now()) -> None:
        """
        Creates a request to create a new record in the Lesson table
        """
        lesson = Lessons(students_id=student_id,
                         lessons_type_id=lessons_type_id,
                         date=date,
                         like_guest=guest)
        self._session.add(lesson)
        self._session.commit()
        self.close()

    def update_lesson(self, lesson_id: int, name: str, value: Union[int, bool, datetime]) -> None:
        """
        Creates a request to update a record in the Lesson table
        """
        self._session.query(Lessons).filter_by(id=lesson_id)\
            .update({name: value})
        self._session.commit()
        self.close()

    def select_all_lessons(self):
        """
        Creates a request to select all records in the Lesson table
        """
        result = self._session.query(Lessons.id,
                                     Lessons.students_id,
                                     Lessons.lessons_type_id,
                                     Lessons.date,
                                     Lessons.payment,
                                     Lessons.like_guest,
                                     LessonsType.type_name,
                                     Students.first_name,
                                     Students.last_name,
                                     Students.phone,).filter(
            Lessons.lessons_type_id == LessonsType.id
        ).filter(
            Lessons.students_id == Students.id
        ).all()

        self.close()
        lesson_records = _convert_in_class(result)
        return lesson_records

    def select_one_lesson(self, lesson_id: int) -> list:
        """
        Creates a request to select one record from the Lesson table
        """
        result = self._session.query(Lessons.id,
                                     Lessons.students_id,
                                     Lessons.lessons_type_id,
                                     Lessons.date,
                                     Lessons.payment,
                                     Lessons.like_guest,
                                     LessonsType.type_name,
                                     Students.first_name,
                                     Students.last_name,
                                     Students.phone,).filter(
            Lessons.lessons_type_id == LessonsType.id
        ).filter(
            Lessons.students_id == Students.id
        ).filter_by(id=lesson_id).all()

        self.close()

        lesson_record = _convert_in_class(result)
        return lesson_record

    def select_one_lesson_filter_by_guest(self, user_id: int) -> Union[list, bool]:
        """
        Creates a request to select one record selected by student_id and like_guest value
        """
        try:
            result = self._session.query(Lessons).filter_by(students_id=user_id,
                                                            like_guest=True).one()
        except NoResultFound:
            self.close()
            return False
        self.close()
        return result

    def select_all_lesson_filter_by_student_id(self, user_id: int) -> Union[list, bool]:
        """
        Creates a request to select one record selected by student_id and like_guest value
        """
        try:
            result = self._session.query(Lessons.id,
                                         Lessons.students_id,
                                         Lessons.lessons_type_id,
                                         Lessons.date,
                                         Lessons.payment,
                                         Lessons.like_guest,
                                         LessonsType.type_name,
                                         Students.first_name,
                                         Students.last_name,
                                         Students.phone,).filter(
                Lessons.lessons_type_id == LessonsType.id
            ).filter(
                Lessons.students_id == Students.id
            ).filter_by(students_id=user_id).all()

        except NoResultFound:
            self.close()
            return False
        self.close()

        lesson_record = _convert_in_class(result)
        return lesson_record

    # Lesson_type table
    def select_all_lesson_types(self) -> list:
        """
        Creates a request to select all records in the Lesson_type table
        """
        result = self._session.query(LessonsType).all()
        self.close()
        return result

    def select_one_lesson_type(self, lesson_type_id: int):
        """
        Creates a request to select one record selected by lesson_type_id
        """
        try:
            result = self._session.query(LessonsType).filter_by(id=lesson_type_id)\
                .one()
        except NoResultFound:
            self.close()
            return False

        except MultipleResultsFound:
            self.close()
            return False

        self.close()
        return result

    # Student table
    def _add_new_student(self, username: str, user_id: str, first_name: str, last_name: str, phone=None, guest_is=True) -> None:
        """
        Creates a request to create a new record in the Student table
        """
        student = Students(username=username,
                           user_id=user_id,
                           first_name=first_name,
                           last_name=last_name,
                           phone=phone,
                           guest_is=guest_is)

        self._session.add(student)
        self._session.commit()
        self.close()

    def select_all_students(self):
        """
        Creates a request to select all records in the Student table
        """
        students = self._session.query(
            Students).filter_by(guest_is=False).all()
        self.close()
        return students

    def select_all_guest(self):
        """
        Creates a request to select all records in the Student table
        """
        students = self._session.query(Students).filter_by(guest_is=True).all()
        self.close()
        return students

    def select_one_student_by_id(self, user_id: int, is_id: bool = False):
        """
        Creates a request to select one record selected by user_id
        """
        try:
            if is_id:
                result = self._session.query(Students).filter_by(id=user_id)\
                    .one()
                self.close()
                return result
            else:
                result = self._session.query(Students).filter_by(user_id=user_id)\
                    .one()
                self.close()
                return result

        except NoResultFound:
            self.close()
            return False

    def update_student(self, user_id: int, name: str, value) -> None:
        """
        Creates a request to update a record in the Student table
        """
        self._session.query(Students).filter_by(id=user_id)\
            .update({name: value})
        self._session.commit()
        self.close()

    # Other functions
    def close(self):
        """
        Close session
        """
        self._session.close()

    def check_user_role(self, user_id: int) -> Union[str, bool]:
        """
        Check user role. when user press /start
        """
        try:
            user = self.select_one_student_by_id(user_id)
            if user:
                if str(user.user_id) == ADMIN_ID:
                    return 'admin'

                if user.guest_is:
                    return 'guest'

                if not user.guest_is:
                    return 'student'
            else:
                return False

        except NoResultFound:
            self.close()
            return False
