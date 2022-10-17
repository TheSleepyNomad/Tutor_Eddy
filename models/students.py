from sqlalchemy import Column, String, Integer, Boolean
from database.database_core import Base


class Students(Base):

    __tablename__ = 'students'

    # table fields
    id = Column(Integer, primary_key=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    patronymic = Column(String, index=True)
    phone = Column(Integer)