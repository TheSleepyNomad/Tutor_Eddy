from sqlalchemy import Column, String, DateTime, \
    Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from models.lessons_type import LessonsType
from models.students import Students
from database.database_core import Base


class Lessons(Base):

    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True)
    lesson_type_id = Column(Integer, ForeignKey('lessons_type.id'))
    student_id = Column(Integer, ForeignKey('students.id'))
    date = data = Column(DateTime)
    pay = Column(Boolean)

    lessons_type = relationship(LessonsType)
    students = relationship(Students)

    def __repr__(self):
        return f"{self.lesson_type_id} {self.student_id} {self.date}"
