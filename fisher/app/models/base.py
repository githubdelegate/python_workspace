
from sqlalchemy import Column, Integer, String, SmallInteger
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from contextlib import contextmanager

class SQLAlchemy(_SQLAlchemy):

    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e :
            self.session.rollback()


db = SQLAlchemy()

class Base(db.Model):
    # create_time = Column('')
    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(SmallInteger, default=1)






