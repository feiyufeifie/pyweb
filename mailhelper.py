#coding=utf-8
from flask.ext.mail import Message, Mail
import config
from extensions import mail


class MailHelper():
    @classmethod
    def send_mail(cls, title, body, to):
        msg = Message(title, recipients=[to], sender=config.DEFAULT_MAIL_SENDER)
        msg.html = body
        mail.send(msg)