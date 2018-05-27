from flask import current_app

from app.libs.helper import is_isbn_or_key
from app.models.base import db, Base
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from  sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import login_mgr
# flask login
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook


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


    def generate_token(self, expiration=600):
        s =  Serializer(current_app.config['SECRET_KEY'], expiration)
        return  s.dumps({'id': self.id}).decode('utf-8')

    @staticmethod
    def reset_password(token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data =  s.loads(token.encode('utf-8'))
        except:
            return False

        uid = data.get('id')
        with db.auto_commit():
            user = User.query.get(uid)
            user.password = new_password
        return True


    # 一个用户不能赠送多本一样的书
    # 一个用户不能同时赠送和索要一本书
    # 这个函数的意思就是 判断当前isbn的这本书 是不是可以添加到心愿清单，先判断有没有这本书，
    # 然后判断是不是已经在当前用户的心愿或者赠送清单中了，都不是才能添加
    def can_save_to_list(self, isbn):
        if is_isbn_or_key(isbn) != 'isbn':
            return False
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first:
            return False
        # 既不在赠送清单 也不再心愿清单才可以添加
        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        if not gifting and not wishing:
            return True
        else:
            return False

@login_mgr.user_loader
def get_user(uid):
    return User.query.get(int(uid))