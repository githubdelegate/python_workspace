from flask import render_template, redirect, current_app, g
from flask import request, flash, url_for
from flask_login import login_user, login_required, logout_user, current_user
from flask_sqlalchemy import get_debug_queries
from app.forms.auth import RegisterForm, LoginForm
from app.models.user import User
from . import web
from app.models.base import db

# from app.forms.auth import RegisterForm, LoginForm, ResetPasswordForm, EmailForm, \
#     ChangePasswordForm
# from app.models.user import User
# from app.models import db
# from app.libs.email import send_email

__author__ = '七月'

# get 注册页面， post 提交注册信息页面
@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('web.login'))
    return  render_template('auth/register.html', form=form)

@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            # 下面的逻辑是登陆后能直接跳转到对应的页面 而不一定是首页
            next = request.args.get('next')
            if not next or not next.startwith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('账号不存在，密码错误')
    return  render_template('auth/login.html', form=form)

@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
@login_required
def change_password():
    pass

@web.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('web.index'))


@web.route('/register/confirm/<token>')
def confirm(token):
    pass
    # if current_user.confirmed:
    #     return redirect(url_for('main.index'))
    # if current_user.confirm(token):
    #     db.session.commit()
    #     flash('You have confirmed your account. Thanks!')
    # else:
    #     flash('The confirmation link is invalid or has expired.')
    # return redirect(url_for('main.index'))


@web.route('/register/ajax', methods=['GET', 'POST'])
def register_ajax():
    pass


