from flask import render_template, flash, redirect, url_for, request
from app import app, log_manager
from .forms import LoginForm
from app.models import User
from app import db
from app.logger import logger, log_manager
import time


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


@app.route('/get', methods=['GET'])
def get_from_table():
    start_time = int(round(time.time() * 1000))
    u = User.query.filter_by(username=request.args.get('username')).first()
    total_time = int(round(time.time() * 1000)) - start_time
    logger.info('{} - {} - time: {}'.format(request.remote_addr, request.method, str(total_time)))

    if u != None:
        return str('username: ' + u.username + ' email: ' + u.email)
    return 'Not Found'


@app.route('/post', methods=['POST'])
def add_to_table():
    start_time = int(round(time.time() * 1000))
    u = User(username=request.args.get('username'), email=request.args.get('email'))

    # verify existance
    pred = User.query.filter_by(username=request.args.get('username')).first()
    if pred != None:
        total_time = int(round(time.time() * 1000)) - start_time
        logger.info('{} - {} - time: {}'.format(request.remote_addr, request.method, str(total_time)))
        return 'Found'

    db.session.add(u)
    db.session.commit()
    total_time = int(round(time.time() * 1000)) - start_time
    logger.info('{} - {} - time: {}'.format(request.remote_addr, request.method, str(total_time)))
    return 'Found'


@app.route('/delete', methods=['DELETE'])
def delete_from_table():
    start_time = int(round(time.time() * 1000))
    user = User.query.filter_by(username=request.args.get('username')).first()

    if user == None:
        return 'Not Found'

    db.session.delete(user)
    db.session.commit()
    total_time = int(round(time.time() * 1000)) - start_time
    logger.info('{} - {} - time: {}'.format(request.remote_addr, request.method, str(total_time)))
    return 'Deleted From Table..'
