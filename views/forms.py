#coding=utf-8
from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField
from wtforms.validators import Required


class LoginForm(Form):
    email = TextField('邮箱：', validators=[Required('请输入邮箱')])
    pwd = PasswordField('密码：', validators=[Required('请输入密码')])
    remember_me = BooleanField('记住密码', default=False)