from flask import render_template, url_for, flash, redirect
from champion_webapp import app
from champion_webapp import db
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

@app.context_processor
def context_processor():
	is_logged_in = db.current_user() is None




	return dict(is_logged_in)


@app.route("/")
@app.route("/home")
def home():
	# flash(db.current_user()==None, 'primary')
	return render_template('home.html', title='Home', posts=data)



# @app.route("/store/<champion>")
# def store(champion):
# 	if champion == '#':
# 		return render_template('store.html', title='Store', database=db)
# 	else:
# 		if db.current_user == None:
# 			flash(f'Please log into your account.')
# 			return rediect(url_for('login'))
# 		else:
# 			flash(f'Added champion {champion} to Account!', 'success')
# 			return render_template('store.html', title='Store', database=db)



@app.route("/store")
def store():
	return render_template('store.html', title='Store')



@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		username = form.username.data
		password = form.password.data
		try:
			db.register(username, password)
			flash(f'Account created for {form.username.data}!', 'success')
			return redirect(url_for('login'))
		except:
			flash(f'Username {form.username.data} already taken!', 'danger')
	return render_template('register.html', title='Register', form=form)



@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		try:
			db.login(form.username.data, form.password.data)
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))
		except:
			flash('Incorrect username or password!', 'danger')
	return render_template('login.html', title='Login', form=form)


# @app.route("/profile", methods=['GET', 'POST'])
# def profile():
# 	return redner_template('profile.html', title='Account', database=db)
@app.route("/logout")
def logout():
	db.logout()
	return redirect('url_for(home)')
