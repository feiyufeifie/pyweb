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

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    @classmethod
    def get_by_id(self, id):
        return self.query.filter(User.id == id).first()

    @classmethod
    def authenticate(self, email, pwd):
        user = self.query.filter(User.email == email).first()
        if user:
            authenticated = user.pwd == pwd
        else:
            authenticated = False
        return user, authenticated

    @classmethod
    def get_by_name(self, username):
        return self.query.filter(User.name == username).first()