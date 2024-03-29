# http://flask.pocoo.org/docs/0.12/patterns/sqlalchemy/
import os.path

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# filepath = os.path.abspath('C://Working//dev//Python//Reporting//test.db')
filepath = os.path.abspath(r'C:\Working\dev\Python\FlaskResterExample\test.db')

engine = create_engine('sqlite:///' + filepath, echo=False)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    Base.metadata.create_all(bind=engine)
