from flask import render_template, flash, redirect, url_for, request
from app import app, log_manager
from .forms import LoginForm
from app.models import User,Post,UserInformation
from app import db
from app.logger import logger, log_manager
import time


def log(ans, start_time):
    total_time = int(round(time.time() * 1000)) - start_time
    logger.info('{} - {} - time: {}'.format(request.remote_addr, request.method, str(total_time)))
    return 'Not Found'


@app.route('/k-means')
def display():
    return log_manager.display()

@app.route('/inject')
def inject():
    total_time = 500
    logger.info('{} - {} - time: {}'.format(request.remote_addr, request.method, str(total_time)))
    return render_template('rain.html')

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Alon'}
    return render_template('index.html', user=user)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/get-user', methods=['GET'])
def get_from_table():
    start_time = int(round(time.time() * 1000))
    u = User.query.filter_by(username=request.args.get('username')).first()
    total_time = int(round(time.time() * 1000)) - start_time
    logger.info('{} - {} - time: {}'.format(request.remote_addr, request.method, str(total_time)))

    if u != None:
        return str('username: ' + u.username + ' email: ' + u.email)
    return 'Not Found'


@app.route('/post-user', methods=['POST'])
def add_to_table():
    start_time = int(round(time.time() * 1000))
    u = User(username=request.args.get('username'), email=request.args.get('email'))

    # verify existence
    pred = User.query.filter_by(username=request.args.get('username')).first()
    if pred != None:
        return log('Found', start_time)

    db.session.add(u)
    db.session.commit()
    return log('Found', start_time)


def delete_user_posts(user):
    #getting all posts of user
    posts = Post.query.all()
    for post in posts:
        db.session.delete(post)
    db.session.commit()

def delete_user_information(user):
    #getting user information
    infos = UserInformation.query.all()
    for info in infos:
        db.session.delete(info)
    db.session.commit()


@app.route('/delete-user', methods=['DELETE'])
def delete_from_table():
    start_time = int(round(time.time() * 1000))
    user = User.query.filter_by(username=request.args.get('username')).first()

    if user == None:
        return log('Not Found', start_time)

    delete_user_posts(user)
    delete_user_information(user)

    db.session.delete(user)
    db.session.commit()
    return log('Deleted From Table..', start_time)

@app.route('/get-post')
def get_post():
    start_time = int(round(time.time() * 1000))
    user = request.args.get('username')
    if user == None:
        return log('Not Found', start_time)

    post = user.posts.first()
    return log(post.body, start_time)


@app.route('/post-post')
def post_post():
    start_time = int(round(time.time() * 1000))
    username = request.args.get('username')
    body = request.args.get('body')
    user = User.query.filter_by(username).first()

    if user == None:
        return log('Not Found', start_time)

    new_post = Post(body=body, author=user)
    db.session.add(new_post)
    db.session.commit()
    return log('Done', start_time)

@app.route('/delete-post')
def delete_post():
    start_time = int(round(time.time() * 1000))
    username = request.args.get('username')
    user = User.query.filter_by(username)

    if user == None:
        return log('User Not Found', start_time)

    post = user.posts.first()
    if post == None:
        return log('no Posts', start_time)
    db.session.delete(post)
    db.session.commit()
    return log('Done', start_time)

def parseInfoArgs(request):
    address = request.args.get('address')
    zip_code = request.args.get('zip_code')
    full_name = request.args.get('full_name')
    age = request.args.get('age')
    return {address: address, zip_code: zip_code, full_name: full_name, age: age}

@app.route('/post-user-information')
def post_user_information():
    start_time = int(round(time.time() * 1000))
    username = request.args.get('username')
    user = User.query.filter_by(username)

    if user ==None:
        return log('User Not Exist', start_time)
    info = user.user_information.first()
    if info != None:
        return log('User Have Information', start_time)
    args = parseInfoArgs(request)
    info = UserInformation(address=args.address, zip_code=args.zip_code, full_name=args.full_name, age=args.age,author=user)
    db.session.add(info)
    db.session.commit()
    return log('Done', start_time)

@app.route('/get-user-information')
def get_user_information():
    start_time = int(round(time.time() * 1000))
    username = request.args.get('username')
    user = User.query.filter_by(username)
    if user == None:
        return log('User not Exist', start_time)
    user_info = user.user_information.first()
    return log('Done', start_time)

@app.route('/change-user-information')
def change_user_information():
    start_time = int(round(time.time() * 1000))
    username = request.args.get('username')
    user = User.query.filter_by(username)
    if user == None:
        return log('User Not Exist', start_time)
    user_info = user.user_information.first()
    if user_info != None:
        db.session.delete(user_info)
        db.session.commit()
    args = parseInfoArgs(request)
    info = UserInformation(address=args.address, zip_code=args.zip_code, full_name=args.full_name, age=args.age, author=user)
    db.session.add(info)
    db.session.commit()
    return log('Done', start_time)