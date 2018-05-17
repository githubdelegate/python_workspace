# from app.libs.email import send_email
# from app.models.gift import Gift
# from app.view_models.wish import MyWishes
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user

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
    pass


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    pass


@web.route('/satisfy/wish/<int:wid>')
@login_required
# @limiter.limit(key_func=limit_key_prefix)
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
@login_required
def redraw_from_wish(isbn):
    pass