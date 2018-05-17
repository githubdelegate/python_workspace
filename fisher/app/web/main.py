# from app.service.gift import GiftService
from flask import render_template, config, current_app, request, url_for
from flask_login import login_required, current_user
from sqlalchemy import desc
from . import web

# from app.models.gift import Gift

__author__ = '七月'


# def __current_user_status_change():
#     r = request


@web.route('/')
# @cache.cached(timeout=100, unless=__current_user_status_change)
# @cache.cached(timeout=100)
def index():
    return 'index'

@web.route('/personal')
@login_required
def personal_center():
    pass
    # return render_template('personal.html', user=current_user.summary)


