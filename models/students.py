from sqlalchemy import Column, String, Integer, Boolean
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
    guest_is = Column(Boolean)

    def __repr__(self):
        return f"{self.last_name} {self.first_name}"
