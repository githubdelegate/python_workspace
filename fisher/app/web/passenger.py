# from flask.ext.sqlalchemy import get_debug_queries
from . import web
# from app import cache
# from app import limiter
from flask import flash, redirect, url_for, request, current_app


@web.after_request
def see_cache(b):
    pass


# @limiter.limited
def satifiy_with_limited():
    isbn = request.args['isbn']
    flash('你已向他发送过赠送邀请，请不要频繁发送')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.after_app_request
def after_request(response):
    pass
