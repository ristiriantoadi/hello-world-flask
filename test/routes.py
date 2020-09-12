from flask import render_template,url_for,flash,redirect
from test import app
from .models import User,Post
from .forms import RegistrationForm,LoginForm

posts=[{
    'title' : 'title 1',
    'author':'coreyms'
    },
    {
    'title' : 'title 2',
    'author':'coreyms'
    },
    {
    'title':'title 3',
    'author':'coreyms'
    }]


@app.route('/home')
def home():
    return render_template("home.html",posts=posts,another="something")

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for '+str(form.username.data),'success')
        return redirect(url_for('home'))
    return render_template("register.html",form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template("login.html",form=form)

@app.route('/halo')
def halo():
    return 'halo dunia'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'My name is '+str(username)