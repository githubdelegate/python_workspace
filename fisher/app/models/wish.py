from app.models.base import db, Base

from  sqlalchemy import  Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Wish(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    launched = Column(Boolean, default=False)
    user = relationship('User')
    uid = Column(Integer,ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
