from flask import Flask,request,make_response,redirect,abort
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    # user_agent = request.headers.get('User-Agent')
    # response = make_response('<p> your browser is %s </p>' % user_agent)
    # response.set_cookie('answer','42')
    # return response
    return redirect('http://www.baidu.com')

@app.route('/user/<name>')
def user(name):
    return '<h1> hello %s </h1>' % name

# @app.route('/user/<id>')
# def get_user(id):
#     user = load_user(id)
#     if not user:
#         abort(404)
#     return '<h1> hello %s </h1>' % user.name
 


if __name__ == '__main__':
    manager.run()

