#!/usr/bin/env python
#coding=utf-8

from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.uploads import UploadSet

__all__ = ['mail', 'db',  'file_set']

mail = Mail()
db = SQLAlchemy()
file_set = UploadSet('file', ('txt','doc', 'docx'))