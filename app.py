from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"
app.config['SECRET_KEY'] = app.secret_key

@app.route('/')
def home():

	if login_session['logged_in']:
		print('aaaa')
		return render_template('home.html', name=login_session['name'])

	return render_template('home.html')

@app.route('/signup')
def sign_up():

	return render_template('signup.html')

@app.route('/adduser', methods=['POST'])
def new_user():

	username = request.form['username']

	if user_exist(username):
		return render_template('home.html', error=True)

	add_user(username, request.form['password'])

	login_session['logged_in'] = True
	login_session['name'] = request.form['username']

	return render_template('home.html', name=login_session['name'])

@app.route('/login')
def log_in():
	return render_template('login.html')

@app.route('/loggedin', methods=['POST'])
def logged_in():

	if not user_exist(request.form['username']):
		return render_template('home.html', error=True)

	elif request.form['password'] != get_pass(request.form['username']):
		return render_template('home.html', error=True)

	login_session['logged_in'] = True
	login_session['name'] = request.form['username']

	return home()

@app.route('/logout')
def log_out():

	login_session['logged_in'] = False
	login_session['name'] = None

	return home()

@app.route('/canvas', methods=['POST'])
def canvas():

	return render_template('canvas.html', data=get_lateset_point(request.form('canvas_id')).data)

@app.route('/save_draw', methods=['POST'])
def save_draw():

	new_history_point(request.form['picData'], request.form['canvasID'])
	return

if __name__ == '__main__':
    app.run(debug=True)