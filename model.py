from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

class User(Base):
	__tablename__ = 'users'

	user_id = Column(Integer, primary_key=True)

	name = Column(String)
	password = Column(String)
