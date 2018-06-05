from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(1024), index=True, unique=True)
    email = db.Column(db.String(1024), index=True, unique=True)
    password_hash = db.Column(db.String(1024))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    user_information = db.relationship('UserInformation', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(1024), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class UserInformation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(1024), index=True)
    zip_code = db.Column(db.String(1024))
    full_name = db.Column(db.String(1024))
    age = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<User {}>'.format(self.full_name)
