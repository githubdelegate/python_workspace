from flask import Flask,request,make_response,redirect,abort,render_template,session,url_for,flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess'
manager = Manager(app)
bootstrap = Bootstrap(app)
monent = Moment(app)

class NameForm(FlaskForm):
    name = StringField('waht is name?',validators=[DataRequired()])
    submit = SubmitField('submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('look like you hava changed your name')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html',form=form,name=session.get('name'))


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

if __name__ == '__main__':
    manager.run()

