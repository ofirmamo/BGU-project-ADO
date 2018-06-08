from flask import render_template, flash, redirect, url_for, request
from app import app, log_manager
from .forms import LoginForm
from app import counters
from app.logger import logger, log_manager, log_manager_user, log_manager_posts, log_manager_userinfo
from app import components
import time

def log(start_time):
    total_time = int(round(time.time() * 1000)) - start_time
    logger.info('{} - {} - time: {}'.format(request.remote_addr, request.method, str(total_time)))
    counters.update_max(total_time)

@app.route('/k-means-server')
def display():
    return log_manager.display()

@app.route('/k-means-user')
def display_user():
    return log_manager_user.display()

@app.route('/k-means-posts')
def display_post():
    return log_manager_posts.display()

@app.route('/k-means-userinfo')
def display_userinfo():
    return log_manager_userinfo.display()

@app.route('/inject')
def inject():
    components.inject_user(request)
    components.inject_post(request)
    components.injcet_userinfo(request)
    total_time = counters.transaction_max
    logger.info('{} - {} - time: {} - injcted'.format(request.remote_addr, request.method, str(total_time)))
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
    u = components.get_user(request)
    log(start_time)
    if u != None:
        return str('username: ' + u.username + ' email: ' + u.email)
    return 'Not Found'


@app.route('/post-user', methods=['POST'])
def add_to_table():
    start_time = int(round(time.time() * 1000))
    components.add_user(request)
    log(start_time)
    return 'Found'


@app.route('/delete-user', methods=['DELETE'])
def delete_from_table():
    start_time = int(round(time.time() * 1000))
    answer = components.delete_user(request)
    log(start_time)
    return answer


@app.route('/get-post', methods=['GET'])
def get_post():
    start_time = int(round(time.time() * 1000))
    answer = components.get_post(request)
    log(start_time)
    if answer == None:
        return 'User Have no Posts'
    return answer


@app.route('/post-post', methods=['POST'])
def post_post():
    start_time = int(round(time.time() * 1000))
    answer = components.add_post(request)
    log(start_time)
    return answer


@app.route('/delete-post', methods=['DELETE'])
def delete_post():
    start_time = int(round(time.time() * 1000))
    answer = components.delete_post(request)
    log(start_time)
    return answer


@app.route('/post-user-information', methods=['POST'])
def post_user_information():
    start_time = int(round(time.time() * 1000))
    answer = components.add_userinfo(request)
    log(start_time)
    return answer


@app.route('/get-user-information', methods=['GET'])
def get_user_information():
    start_time = int(round(time.time() * 1000))
    user_info = components.get_userinfo(request)
    log(start_time)
    if user_info == None:
        return 'User have no information'
    return user_info


@app.route('/change-user-information', methods=['POST'])
def change_user_information():
    start_time = int(round(time.time() * 1000))
    answer = components.change_userinfo(request)
    log(start_time)
    return answer
