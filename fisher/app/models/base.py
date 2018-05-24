
from sqlalchemy import Column, Integer, String, SmallInteger
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from contextlib import contextmanager


# 这里使用了contextmanager 上下文管理器 实现了
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
    # 提示flask 不要创建base 这个表
    __abstract__ = True
    # create_time = Column('')
    status = Column(SmallInteger, default=1)


# python 动态特性，更加字典 给属性赋值
    def set_attrs(self, attr_dict):
        for key, value in attr_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)






