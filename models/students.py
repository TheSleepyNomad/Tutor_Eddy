from sqlalchemy import Column, String, Integer
from database.database_core import Base


class Students(Base):

    __tablename__ = 'students'

    # table fields
    id = Column(Integer, primary_key=True)
    username = Column(String, index=True)
    user_id = Column(Integer)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    phone = Column(Integer)

    def __repr__(self):
        return f"{self.second_name} {self.first_name}"
