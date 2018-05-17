from app.models.base import db, Base

from  sqlalchemy import  Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationships, For

class Gift(Base):
    launched = Column(Boolean, default=False)
    user = relationships('User')
    uid = Column(Integer,ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
