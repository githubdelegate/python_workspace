# from app.libs.enums import PendingStatus
# from app.models.drift import Drift
# from flask import render_template, flash, request, redirect, url_for, current_app
# from flask_login import login_required, current_user
# from sqlalchemy import desc, func
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
    pass


@login_required
@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    gift = Gift()
    gift.isbn = isbn
    gift.uid = current_user.id
    pass


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
