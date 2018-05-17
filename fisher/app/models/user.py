
from app.models.base import db, Base

from  sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# flask login
class User(UserMixin, Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(24), nullable=False)
    phone = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))
    # 第一个参数表示指定字段名
    _password = Column('password', String(128), nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    # flask login 指定函数
    def get_id(self):
        return self.id

# @login_mgr.user_loader
# def get_user(uid):
#     return User.query.get(uid)