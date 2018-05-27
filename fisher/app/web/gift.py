# from app.libs.enums import PendingStatus
# from app.models.drift import Drift
# from flask import render_template, flash, request, redirect, url_for, current_app
# from flask_login import login_required, current_user
# from sqlalchemy import desc, func

from flask import current_app, flash, render_template, url_for, redirect

from app.models.base import db
from app.models.gift import Gift
from . import web
# from app.spider.yushu_book import YuShuBook
# from app.view_models.gift import MyGifts
# from app.service.gift import GiftService

# from app.models import db
# from app.models.gift import Gift

from flask_login import login_required, current_user

__author__ = '七月'


@login_required
@web.route('/my/gifts')
def my_gifts():
    uid = current_user.id
    gifts_of_mine = Gift.get_user_gift(uid)
    isbn_list = [gift.isbn for gift in gifts_of_mine]



@login_required
@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        # 数据库的回滚，
        # try:
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
            # db.session.commit()
        # except Exception as e:
        #     db.session.rollback()
        #     raise e
    else:
        flash('这本书已经在赠送清单 或者在心愿清单')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
