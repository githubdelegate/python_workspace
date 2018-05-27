from flask import Blueprint, render_template

web = Blueprint('web', __name__)


# flask  定义的错误处理  AOP思想
@web.app_errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


from app.web import book
from app.web import auth
from app.web import drift
from app.web import errors
from app.web import gift
from app.web import main
from app.web import wish
# from app.web import passenger
