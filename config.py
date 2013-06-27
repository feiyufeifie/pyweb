DEBUG = True
SECRET_KEY = '!@#$%QWERT'

SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/python?charset=utf8'
SQLALCHEMY_ECHO = False

UPLOADS_DEFAULT_DEST = '/upload'
UPLOADS_DEFAULT_URL = '/file'

MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = DEBUG
MAIL_USERNAME = 'pythonweb'
MAIL_PASSWORD = '12qwaszx'
DEFAULT_MAIL_SENDER = 'pythonweb@163.com'

ENCRYPTION_KEY = '1qaz2wsx'

BABEL_DEFAULT_TIMEZONE = 'Asia/Shanghai'

DEBUG_LOG = 'logs/debug.log'
ERROR_LOG = 'logs/error.log'