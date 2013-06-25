#!/usr/bin/env python
#coding=utf-8

from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy

__all__ = ['mail', 'db']

mail = Mail()
db = SQLAlchemy()