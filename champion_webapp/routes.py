from flask import render_template, url_for, flash, redirect
from champion_webapp import app
from champion_webapp.forms import RegistrationForm, LoginForm


data = [
	{
		'author': 'Eddy Liang',
		'title': 'Space marine forward base report',
		'content': 'Weather is clear. Bolters loaded. For the empire!',
		'date_posted': '01/22/2021'
	},
	{
		'author': 'Conor McGregor',
		'title': 'UFC 257 report day 3',
		'content': 'Put up the red panties, were rich baby',
		'date_posted': '01/26/2021'
	},
]


# @app.route("/")
# def welcome():
# 	return render_template('welcome.html')

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=data)


@app.route("/about")
def about():
	return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Incorrect username or password!', 'danger')
	return render_template('login.html', title='Login', form=form)
