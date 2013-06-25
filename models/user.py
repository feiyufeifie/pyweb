#coding=utf-8
from datetime import datetime
from flask.ext.sqlalchemy import BaseQuery
from extensions import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    pwd = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.SmallInteger, default=0)
    add_date = db.Column(db.DateTime, default=datetime.utcnow)
    last_update_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, email, pwd, gender=0):
        self.name = name
        self.email = email
        self.pwd = pwd
        self.gender = gender

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter(User.id == id).first()

    @classmethod
    def authenticate(cls, email, pwd):
        user = cls.query.filter(User.email == email).first()
        if user:
            authenticated = user.pwd == pwd
        else:
            authenticated = False
        return user, authenticated

    @classmethod
    def get_by_name(cls, username):
        return cls.query.filter(User.name == username).first()

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter(User.email == email).first()

    @classmethod
    def add(cls, name, email, pwd):
        db.session.add(User(name, email, pwd))
        db.session.commit()
        return cls.get_by_email(email)