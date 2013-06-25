#coding=utf-8
from flask import Module, render_template, redirect, flash, url_for, g
from flask.ext.login import login_user, logout_user
from flask.ext.mail import Message
from extensions import mail, config
from models import User
from views.forms import RegForm, LoginForm, FindPwdForm


account = Module(__name__)


@account.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index.home'))

    msg = None
    form = LoginForm()
    if form.validate_on_submit():
        (user, authenticated) = User.authenticate(str(form.email.data), str(form.pwd.data))
        if(authenticated):
            login_user(user, bool(form.remember_me.data))
            return redirect(url_for('index.home'))
        else:
            msg = '用户名或密码错误，请重新输入'
    return render_template('account/login.html', msg=msg, form = form)


@account.route('/reg', methods=['GET', 'POST'])
def reg():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index.home'))

    msg = None
    form = RegForm()
    if form.validate_on_submit():
        email = str(form.email.data)
        user = User.get_by_email(email)
        if user:
            msg = '邮箱已存在，请更换邮箱'
        else:
            user = User.add(str(form.name.data), email, str(form.pwd.data))
            if user:
                login_user(user, bool(form.remember_me))
                return redirect(url_for('index.home'))
            else:
                msg = '注册出错'
    return render_template('account/reg.html', msg=msg, form=form)


@account.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('index.home'))


@account.route('/findpwd', methods=['GET', 'POST'])
def findpwd():
    msg = None
    email = None
    form = FindPwdForm()
    user = None
    if form.validate_on_submit():
        email = str(form.email.data)
        user = User.get_by_email(email)
        if user:
            mail.send_mail('测试', '<b>testing</b>', email)
        else:
            msg = '该邮箱没有注册，请核对信息'

    return render_template('account/findpwd.html', msg=msg, email=email, user=user, form=form)