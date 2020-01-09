from model import Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# engine = create_engine('sqlite:///database.db')
# Base.metadata.create_all(engine)
# DBSession = sessionmaker(bind=engine)
# session = DBSession()


def create_thread():
	engine = create_engine('sqlite:///database.db')
	Base.metadata.create_all(engine)
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
	return session

def add_user(name, password):

	session = create_thread()
	user = User(name=name, password=password)

	session.add(user)
	session.commit()

def get_pass(name):

	session = create_thread()

	return session.query(User).filter_by(name=name).first().password

def user_exist(name):

	session = create_thread()

	user = session.query(User).filter_by(name=name).first()

	return user is not None