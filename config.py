DEBUG = True
SECRET_KEY = '!@#$%QWERT'

SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/python?charset=utf8'
SQLALCHEMY_ECHO = False

UPLOADS_DEFAULT_DEST = '/path/to/pypress/static/'
UPLOADS_DEFAULT_URL = '/static'

BABEL_DEFAULT_TIMEZONE = 'Asia/Shanghai'

PER_PAGE = 20

DEBUG_LOG = 'logs/debug.log'
ERROR_LOG = 'logs/error.log'

MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = DEBUG
MAIL_USERNAME = 'pythonweb'
MAIL_PASSWORD = '12qwaszx'
DEFAULT_MAIL_SENDER = 'pythonweb@163.com'
