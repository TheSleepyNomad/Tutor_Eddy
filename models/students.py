from sqlalchemy import Column, String, Integer
from database.database_core import Base


class Students(Base):

    __tablename__ = 'students'

    # table fields
    id = Column(Integer, primary_key=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    patronymic = Column(String, index=True)
    phone = Column(Integer)

    def __repr__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"
