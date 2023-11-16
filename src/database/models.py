from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import Date
from sqlalchemy.ext.declarative import declarative_base

from src.database.db import engine

Base = declarative_base()

class Contacts(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(60), nullable=False)
    email = Column(String(30), nullable=False)
    phone_number = Column(String(20), nullable=False)
    birth_date = Column(Date, nullable=False)
    description = Column(String(300), nullable=True)