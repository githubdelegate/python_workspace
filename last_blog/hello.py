from flask import Flask,request,make_response,redirect,abort,render_template,session,url_for,flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate,MigrateCommand
from flask_mail import Mail,Message
from threading import Thread

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ddd0@qq.com'
app.config['MAIL_PASSWORD'] = 'ddd'
app.config['FLASK_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'xxxcom'
app.config['FLASKY_ADMIN'] = 'xxx'


manager = Manager(app)
bootstrap = Bootstrap(app)
monent = Moment(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

mail = Mail(app)


class NameForm(FlaskForm):
    name = StringField('waht is name?',validators=[DataRequired()])
    submit = SubmitField('submit')

def send_async_mail(app,msg):
    with app.app_context():
        mail.send(msg)

def send_mail(to, subject,template,**kwargs):
    msg = Message(app.config['FLASK_MAIL_SUBJECT_PREFIX'] + subject, sender = app.config['FLASKY_MAIL_SENDER'],recipients=[to])
    msg.body = render_template(template + '.txt',**kwargs)
    msg.html = render_template(template + '.html',**kwargs)

    thr = Thread(target=send_async_mail,args=[app,msg])
    thr.start()
    return thr


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            session['know'] = False
            if app.config['FLASKY_ADMIN']:
                send_mail(app.config['FLASKY_ADMIN'],'new user','mail/new_user',user=user)
        else:
            session['know'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html',form = form,name = session.get('name'),know = session.get('know'))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

# @app.route('/user/<id>')
# def get_user(id):
#     user = load_user(id)
#     if not user:
#         abort(404)
#     return '<h1> hello %s </h1>' % user.name
 
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internam_server_error(e):
    return render_template('500.html'), 500

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    users = db.relationship('User',backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name
 

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))


    def __repr__(self):
        return '<User %r>' % self.username
 

if __name__ == '__main__':
    manager.run()

