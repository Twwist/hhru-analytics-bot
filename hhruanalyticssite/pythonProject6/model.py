from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Row(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    age = Column(Integer)
    area = Column(String(255))
    certificate = Column(String(255))
    level = Column(String(255))
    primary_name = Column(String(255))
    primary_organization = Column(String(255))
    primary_result = Column(String(255))
    primary_year = Column(Integer)
    company = Column(String(255))
    start = Column(DateTime)
    end = Column(DateTime)
    industry = Column(String(255))
    position = Column(String(255))
    first_name = Column(String(255))
    gender = Column(String(255))
    last_name = Column(String(255))
    middle_name = Column(String(255))
    resume = Column(String(1000))
    amount = Column(Integer)
    currency = Column(String(255))
    title = Column(String(255))
    total_experience = Column(Integer)
    phone = Column(String(255))
    email = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    favourites = Column(Boolean)