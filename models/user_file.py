#coding=utf-8
from datetime import datetime
from extensions import db


class UserFile(db.Model):
    __tablename__ = 'userfile'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, index=True)
    name = db.Column(db.VARCHAR(100))
    add_date = db.Column(db.DateTime, default=datetime.utcnow)
    last_update_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter(UserFile.name == name).first()

    @classmethod
    def find_by_userid(cls, user_id):
        return cls.query.filter(UserFile.user_id == user_id).all()

    @classmethod
    def add(cls, user_id, name):
        db.session.add(UserFile(user_id, name))
        db.session.commit()
        return cls.get_by_name(name)

    @classmethod
    def update(cls, user_file):
        db.session.add(user_file)
        db.session.commit()
        return cls.get_by_email(user_file.id)
