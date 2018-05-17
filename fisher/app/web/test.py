from time import sleep

# from app.libs.http import Http
# from app.models.test import Test1
from . import web
from flask import session, request


@web.route('/session')
def test_session():
    session['test'] = 123
    return ''

@web.route('/record')
def test_reord():
    s = request.remote_addr
    return s

@web.route('/test')
def test_ip():
    pass

@web.route('/get/session')
def get_test_session():
    t = session['_fresh']
    return str(t)

s = 'insert into table values (%s, %s, %s)' % (1,2,3)




