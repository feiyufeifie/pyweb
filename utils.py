#coding=utf-8
import base64
from flask.ext.mail import Message
from flask.ext.uploads import *
from pyDes import des, CBC, PAD_PKCS5
from werkzeug.utils import secure_filename
import config
from extensions import mail


class MailUtil():
    @classmethod
    def send_mail(cls, title, body, to):
        msg = Message(title, recipients=[to], sender=config.DEFAULT_MAIL_SENDER)
        msg.html = body
        mail.send(msg)


class EncryptionUtil():
    @classmethod
    def encrypt(cls, data):
        k = des(config.ENCRYPTION_KEY, CBC, "\0\0\0\0\0\0\0\0", padmode=PAD_PKCS5)
        return base64.b32encode(k.encrypt(data))

    @classmethod
    def decrypt(cls, data):
        k = des(config.ENCRYPTION_KEY, CBC, "\0\0\0\0\0\0\0\0", padmode=PAD_PKCS5)
        return k.decrypt(base64.b32decode(data))