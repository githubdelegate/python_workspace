from flask import Flask
from app.models.base import db
from flask_login import LoginManager

login_mgr = LoginManager()
def create_app():
    app = Flask(__name__)
    print(id(app))
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    login_mgr.init_app(app)
    login_mgr.login_view = 'web.login'
    login_mgr.login_message = '请登录'
    db.init_app(app)
    db.create_all(app=app)

    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)