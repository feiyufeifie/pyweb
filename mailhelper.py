#coding=utf-8
from flask.ext.mail import Message, Mail
from extensions import config, mail


class MailHelper():
    @classmethod
    def send_mail(cls, title, body, to):
        msg = Message(title, recipients=[to], sender=config['DEFAULT_MAIL_SENDER'])
        msg.html = body
        cls.send(msg)