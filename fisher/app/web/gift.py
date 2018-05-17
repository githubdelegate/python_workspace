# from app.libs.enums import PendingStatus
# from app.models.drift import Drift
# from flask import render_template, flash, request, redirect, url_for, current_app
# from flask_login import login_required, current_user
# from sqlalchemy import desc, func

from . import web
# from app.spider.yushu_book import YuShuBook
# from app.view_models.gift import MyGifts
# from app.service.gift import GiftService

# from app.models import db
# from app.models.gift import Gift

__author__ = '七月'


@web.route('/my/gifts')
def my_gifts():
    pass


@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    pass

@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
