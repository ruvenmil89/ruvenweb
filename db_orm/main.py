from sqlalchemy import Column,Integer,String,ForeignKey,DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///testing.db', echo=True)


class Users(Base):

    __tablename__ = 'userstesting'
    id = Column(Integer, primary_key=True)
    name = Column(String(20),nullable=False)
    lastname = Column(String(20),nullable=False)
    timecreate = Column(DateTime(timezone=True), server_default=func.now())
    timeupdated = Column(DateTime(timezone=True), onupdate=func.now())
    age = Column(Integer,nullable=False)
    company = Column(String(10),nullable=False)

    def __repr__(self):
        return f' user: {self.name}, lastname: {self.lastname} company: {self.company}'


