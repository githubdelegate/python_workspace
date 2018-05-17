# from app.forms.book import DriftForm
# from app.service.drift import DriftService
# from app.libs.enums import PendingStatus
# from app.models.base import db
# from app.models.drift import Drift
# from app.models.wish import Wish
# from app.view_models.drift import DriftViewModel
# from flask import render_template, flash, request, redirect, url_for, current_app
# from flask_login import login_required, current_user
# from sqlalchemy import or_, desc
# from app import cache

from . import web
from flask_login import login_required
# from app.models.gift import Gift

__author__ = '七月'


@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
@login_required
def send_drift(gid):
    pass

@web.route('/pending')
@login_required
def pending():
    pass


@web.route('/drift/<int:did>/reject')
@login_required
def reject_drift(did):
    pass

@web.route('/drift/<int:did>/redraw')
@login_required
def redraw_drift(did):
    pass


@web.route('/drift/<int:did>/mailed')
@login_required
def mailed_drift(did):
   pass
