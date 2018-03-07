import time
from flask import render_template, flash, redirect, url_for, request
from ..app import app
from forms import LoginForm
from ..app.models import User
from ..app import db
from ..app.logger import logger
from LogsManager import LogsManager

logManager: LogsManager = LogsManager()


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'dalit'}
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
    if to_log(total_time):
        logger.info('transaction time: ' + str(total_time))
    return str('username: ' + u.username + ' email: ' + u.email)


@app.route('/post', methods=['POST'])
def add_to_table():
    start_time = int(round(time.time() * 1000))
    u = User(username=request.args.get('username'), email=request.args.get('email'))
    db.session.add(u)
    db.session.commit()
    total_time = int(round(time.time() * 1000)) - start_time
    if to_log(total_time):
        logger.info('transaction time: ' + str(total_time))
    return 'hello'


@app.route('/delete', methods=['DELETE'])
def delete_from_table():
    start_time = int(round(time.time() * 1000))
    user = User.query.filter_by(username=request.args.get('username')).first()
    db.session.delete(user)
    db.session.commit()
    total_time = int(round(time.time() * 1000)) - start_time
    if to_log(total_time):
        logger.info('transaction time: ' + str(total_time))
    return 'hello'


def to_log(total_time: int):
    toLog: bool = logManager.manage(total_time)
    if toLog:
        logger.info('transaction time: {}'.format(total_time))
