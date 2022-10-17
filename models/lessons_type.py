from sqlalchemy import Column, String, Integer, Boolean
from database.database_core import Base


class LessonsType(Base):

    __tablename__ = 'lessons_type'

    # table fields
    id = Column(Integer, primary_key=True)
    # type Math/English and other
    type_name = Column(String)

    def __repr__(self):
        return f"{self.type_name}"