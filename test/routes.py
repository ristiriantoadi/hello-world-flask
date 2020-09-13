from flask import render_template,url_for,flash,redirect
from test import app, mongo
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

@app.route('/user/add')
def add_user():
    userCollection = mongo.db.user
    userCollection.insert({'name':'harry potter','password':'123','gender':'boy'})
    userCollection.insert({'name':'remus lupin','password':'111'})
    return "add a user"

@app.route('/user/find')
def find_user():
    userCollection = mongo.db.user
    # userCollection.insert({'name':'risti','password':'123','gender':'boy'})
    user=userCollection.find_one({'name':'risti'})
    # return "{user['name']}"
    # app.logger.info('logged in successfully')
    return user['name']+" "+user['gender']

@app.route('/user/find-many')
def find_users():
    userCollection = mongo.db.user
    # userCollection.insert({'name':'risti','password':'123','gender':'boy'})
    users=userCollection.find({'gender':'boy'})
    # for user in users:
    #     app.logger.info(user['name'])
    return render_template("users.html",users=users)
    # return "{user['name']}"
    # return user['name']+" "+user['gender']

@app.route('/user/update')
def update_user():
    userCollection = mongo.db.user
    # userCollection.insert({'name':'risti','password':'123','gender':'boy'})
    user=userCollection.find_one({'name':'risti'})
    # return "{user['name']}"
    user['rumah'] = "home"
    user['password']='111'
    user['usia'] += 2
    userCollection.save(user)
    return "updated a user"

@app.route('/user/delete')
def delete_user():
    userCollection = mongo.db.user
    user=userCollection.find_one({'name':'risti'})
    userCollection.remove(user)
    return "remove "+str(user['name'])

#this one doesnt work
# @app.route('/user/delete-many')
# def delete_users():
#     userCollection = mongo.db.user
#     users=userCollection.find({'password':'123'})
#     userCollection.deleteMany(users)
#     return "remove many users"
