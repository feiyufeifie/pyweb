#coding=utf-8
from flask.ext.wtf import Form, file_required, file_allowed
from wtforms import TextField, BooleanField, PasswordField, HiddenField, FileField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Required


class LoginForm(Form):
    email = EmailField('邮箱：', validators=[Required('请输入邮箱')])
    pwd = PasswordField('密码：', validators=[Required('请输入密码')])
    remember_me = BooleanField('记住密码', default=False)


class RegForm(Form):
    name = TextField('昵称：', validators=[Required('请输入昵称')])
    email = EmailField('邮箱：', validators=[Required('请输入邮箱')])
    pwd = PasswordField('密码：', validators=[Required('请输入密码')])
    remember_me = BooleanField('记住密码', default=False)


class FindPwdForm(Form):
    email = EmailField('邮箱：', validators=[Required('请输入邮箱')])


class ResetPwdForm(Form):
     pwd = PasswordField('密码：', validators=[Required('请输入密码')])
     token = HiddenField('token')


class UploadFileForm(Form):
     file = FileField('选择文件：', validators=[Required('请选择文件')])