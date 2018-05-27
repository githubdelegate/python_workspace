from threading import Thread

from flask import current_app, render_template
from flask_mail import Message

from app import mail


def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
         except Exception as e:
             pass


def send_mail(to, subject, template, **kwargs):
    # msg = Message('xxxx', sender='xxxx', body='sss', recipients=['xxxx'])
    msg = Message('[xxx]' + subject, sender=current_app.config['MAIL_SENDER'], recipients=[to])
    msg.html = render_template(template, **kwargs)
    # 这里注意 异步编程 app对象获取
    app = current_app._get_current_object()
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    # mail.send(msg)
