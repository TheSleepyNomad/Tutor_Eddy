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
from datetime import datetime


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
        lesson = Lessons(students_id=student_id, lessons_type_id=lessons_type_id, date=date,
                         like_guest=guest)
        self._session.add(lesson)
        self._session.commit()
        self.close()
    
    def update_lesson(self, lesson_id: int, name: str, value) -> None:
        self._session.query(Lessons).filter_by(
            id=lesson_id).update({name: value})
        self._session.commit()
        self.close()

    def select_all_lessons(self):
        result = self._session.query(
            Lessons.id,
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

    def select_one_lesson(self, lesson_id: int):
        result = self._session.query(
            Lessons.id,
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
        print(type(lesson_record) + '001001')
        return lesson_record

    def select_one_lesson_filter_by_guest(self, user_id: int):
        try:
            result = self._session.query(
                Lessons).filter_by(students_id=user_id, like_guest=True).one()
        except NoResultFound:
            self.close()
            return False
        self.close()
        return result
    
    # Lesson_type table
    def select_all_lesson_types(self):
        result = self._session.query(LessonsType).all()
        self.close()
        print(type(result))
        return result
    
    def select_one_lesson_type(self, lesson_type_id: int):
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

    # Student table
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

    def select_all_students(self):
        students = self._session.query(
            Students).all()
        self.close()
        return students

    def get_user_by_user_id(self, user_id: int):
        result = self._session.query(
            Students).filter_by(user_id=user_id).one()
        self.close()
        return result

    def update_student_profile(self, user_id: int, name: str, value) -> None:
        self._session.query(Students).filter_by(
            user_id=user_id).update({name: value})
        self._session.commit()
        self.close()
    
    def check_user_on_exist_by_user_id(self, user_id: int) -> bool:
        try:
            result = self._session.query(
                Students).filter_by(user_id=user_id).one()
            self.close()
            return result

        except NoResultFound:
            self.close()
            return False
    

    # Other functions
    def close(self):
        """
        Close session
        """
        self._session.close()

    def check_user_role(self, user_id: int) -> str:
        try:
            user = self.check_user_on_exist_by_user_id(user_id)
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

    # ! Important
    # Todo del one of them. check_user_on_exist_by_user_id or get_user_by_user_id
    # Todo and rename
    # Todo check links on functions and repair them all
    

    

    

    

    

    

    

    

    

    

    

    

    