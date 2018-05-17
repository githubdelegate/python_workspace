
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy
from app.models.base import Base

class Book(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='zy')
    isbn = Column(String(15), nullable=False, unique=True)
    price = Column(String(20))
    binding = Column(String(20))
    publisher = Column(String(50))
    pubdate = Column(String(20))
    summary = Column(String(1000))
    image = Column(String(50))
    pages = Column(Integer)


