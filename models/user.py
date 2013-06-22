#coding=utf-8
from datetime import datetime
from flask.ext.sqlalchemy import BaseQuery
from extensions import db


class UserQuery(BaseQuery):
    def from_identity(self, identity):
        try:
            user = self.get(int(identity.name))
        except ValueError:
            user = None
        if user:
            identity.provides.update(user.provides)
        identity.user = user
        return user

    def authenticate(self, email, password):
        user = self.filter(User.email == email).first()
        if user:
            authenticated = user.check_password(password)
        else:
            authenticated = False
        return user, authenticated

    def get_by_name(self, username):
        return self.filter(User.name == username).first()


class User(db.Model):

    __tablename__ = 'user'
    query_class = UserQuery

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    pwd = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.SmallInteger, default=0)
    add_date = db.Column(db.DateTime, default=datetime.utcnow)
    last_update_date = db.Column(db.DateTime, default=datetime.utcnow)