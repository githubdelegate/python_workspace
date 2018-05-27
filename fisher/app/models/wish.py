from app.models.base import db, Base

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, desc, func
from sqlalchemy.orm import relationship




class Wish(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    launched = Column(Boolean, default=False)
    user = relationship('User')
    uid = Column(Integer,ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)


    @classmethod
    def get_user_wishes(cls, uid):
        gifts = Wish.query.filter_by(uid=uid, launched=False).order_by(desc(Wish.create_time)).all()
        return gifts

    @classmethod
    def get_gift_connts(cls, isbn_list):
        from app.models.gift import Gift
        # 这种查询方法的好处，用处
        count_list = db.session.query(func.count(Gift.id), Gift.isbn).filter(
            Wish.launched == False, Gift.isbn.in_(
                isbn_list), Gift.status == 1).group_by(
            Gift.isbn).all()
        count_list = [{'count': w[0], 'isbn': w[1] } for w in count_list]
        return count_list