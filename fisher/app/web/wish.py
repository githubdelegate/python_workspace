# from app.libs.email import send_email
# from app.models.gift import Gift
# from app.view_models.wish import MyWishes
from flask import render_template, flash, redirect, url_for, request, current_app
from flask_login import login_required, current_user

from app.models.base import db
from app.models.wish import Wish
from app.view_models.wish import MyWishes
from . import web
from app.spider.yushu_book import YuShuBook
# from app.service.wish import WishService
# from app import limiter

# from app.models import db
# from app.models.wish import Wish

__author__ = '七月'


def limit_key_prefix():
    isbn = request.args['isbn']
    uid = current_user.id
    return f"satisfy_wish/{isbn}/{uid}"

@web.route('/my/wish')
@login_required
def my_wish():
    uid = current_user.id
    wishes = Wish.get_user_wishes(uid)
    isbn_list = [wish.isbn for wish in wishes]
    gift_count_list = Wish.get_gift_connts(isbn_list)
    view_model = MyWishes(wishes,gift_count_list)
    render_template('my_wish.html', wishes=view_model.gifts)


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        # 数据库的回滚，
        # try:
        with db.auto_commit():
            wish = Wish()
            wish.isbn = isbn
            wish.uid = current_user.id
            db.session.add(wish)
    else:
        flash('这本书已经在赠送清单 或者在心愿清单')
    return redirect(url_for('web.book_detail', isbn=isbn))



@web.route('/satisfy/wish/<int:wid>')
@login_required
# @limiter.limit(key_func=limit_key_prefix)
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
@login_required
def redraw_from_wish(isbn):
    pass