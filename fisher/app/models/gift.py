from flask import current_app

from app.models.base import db, Base

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, desc, func
from sqlalchemy.orm import relationship

# 业务模型
from app.spider.yushu_book import YuShuBook




class Gift(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    launched = Column(Boolean, default=False)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)

# gift 类下面的业务函数
    @classmethod
    def recent(cls):
        recent_gifts = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            Gift.create_time).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        return recent_gifts

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    def get_user_gift(cls, uid):
        gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(desc(Gift.create_time)).all()
        return gifts

    @classmethod
    def get_wish_connts(cls, isbn_list):
        from app.models.wish import Wish
        # 这种查询方法的好处，用处
        count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(
            Wish.launched == False, Wish.isbn.in_(
                isbn_list), Wish.status == 1).group_by(
            Wish.isbn).all()
        count_list = [{'count': w[0], 'isbn': w[1] } for w in count_list]
        return count_list