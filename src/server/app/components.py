from flask import request
from app.models import User, Post, UserInformation
from app import db
from app.logger import user_logger, post_logger, user_information_logger, log_manager
from app import counters
import time

from app.counters import get_total_time


def log(start_time, current_logger, updater):
    total_time = int(round(time.time() * 1000)) - start_time
    current_logger.info('{} - {} - time: {}'.format(request.remote_addr, request.method, str(total_time)))
    updater(total_time)


def delete_user_posts(user):
    # getting all posts of user
    posts = Post.query.all()
    for post in posts:
        db.session.delete(post)
    db.session.commit()


def delete_user_information(user):
    # getting user information
    infos = UserInformation.query.all()
    for info in infos:
        db.session.delete(info)
    db.session.commit()


def parseInfoArgs(request):
    address = request.args.get('address')
    zip_code = request.args.get('zip_code')
    full_name = request.args.get('full_name')
    age = request.args.get('age')
    return {address: address, zip_code: zip_code, full_name: full_name, age: age}


# user component
def get_user(request):
    start_time = int(round(time.time() * 1000))
    u = User.query.filter_by(username=request.args.get('username')).first()
    total_time = int(round(time.time() * 1000)) - start_time
    user_logger.info('{} - {} - time: {}'.format(request.remote_addr, request.method, str(total_time)))
    counters.update_user_max(total_time)
    return u


def add_user(request):
    start_time = int(round(time.time() * 1000))
    u = User(username=request.args.get('username'), email=request.args.get('email'))
    pred = User.query.filter_by(username=request.args.get('username')).first()
    if pred is not None:
        log(start_time, user_logger, counters.update_user_max)
        return
    db.session.add(u)
    db.session.commit()
    log(start_time, user_logger, counters.update_user_max)


def delete_user(request):
    start_time = int(round(time.time() * 1000))
    user = get_user(request)
    if user is None:
        log(start_time, user_logger)
        return 'Uset Not Exist'
    delete_user_posts(user)
    delete_user_information(user)
    db.session.delete(user)
    db.session.commit()
    log(start_time, user_logger, counters.update_user_max)
    return 'Done'


def inject_user(request):
    total_time = get_total_time('user')
    if total_time != 0:
        user_logger.info('{} - {} - time: {} - injected'.format(request.remote_addr, request.method, str(total_time + 100)))


# post component
def get_post(request):
    start_time = int(round(time.time() * 1000))
    username = get_user(request)
    if username is None:
        return 'User Not Found'
    post = username.posts.first()
    log(start_time, post_logger, counters.update_post_max)
    if post is None:
        return None
    return post.body


def add_post(request):
    start_time = int(round(time.time() * 1000))
    body = request.args.get('body')
    user = get_user(request)
    if user is None:
        return 'User Not Found'
    new_post = Post(body=body, author=user)
    db.session.add(new_post)
    db.session.commit()
    log(start_time, post_logger, counters.update_post_max)
    return 'Done'


def delete_post(request):
    start_time = int(round(time.time() * 1000))
    user = get_user(request)
    if user is None:
        return 'User Not Found'
    post = get_post(request)
    if post is None:
        return 'User Have No Posts'

    db.session.delete(post)
    db.session.commit()
    log(start_time, post_logger, counters.update_post_max)
    return 'OK'


def inject_post(requset):
    total_time = get_total_time('post')
    if total_time != 0:
        post_logger.info('{} - {} - time: {} - injected'.format(request.remote_addr, request.method, str(total_time)))


# user information component

def get_userinfo(request):
    start_time = int(round(time.time() * 1000))
    user = get_user(request)
    if user is None:
        return 'User Not Exist'
    user_info = user.user_information.first()
    log(start_time, user_information_logger, counters.update_userinfo_max)
    return user_info


def change_userinfo(requset):
    start_time = int(round(time.time() * 1000))
    user = get_user(request)
    if user is None:
        return 'User Not Exist'
    user_info = get_userinfo(request)
    if user_info is not None:
        db.session.delete(user_info)
        db.session.commit()
    args = parseInfoArgs(request)
    info = UserInformation(address=args.address, zip_code=args.zip_code, full_name=args.full_name, age=args.age,
                           author=user)
    db.session.add(info)
    db.session.commit()
    log(start_time, user_information_logger, counters.update_userinfo_max)
    return 'OK'


def add_userinfo(request):
    start_time = int(round(time.time() * 1000))
    user = get_userinfo(request)
    if user is None:
        return 'User Not Exist'
    info = get_userinfo(request)
    if info is not None:
        return 'User Have User Information'
    args = parseInfoArgs(request)
    info = UserInformation(address=args.address, zip_code=args.zip_code, full_name=args.full_name, age=args.age,
                           author=user)
    db.session.add(info)
    db.session.commit()
    log(start_time, user_information_logger, counters.update_userinfo_max)
    return 'OK'


def injcet_userinfo(requset):
    total_time = get_total_time('userinfo')
    if total_time != 0:
        user_information_logger.info(
            '{} - {} - time: {} - injected'.format(request.remote_addr, request.method, str(total_time)))
