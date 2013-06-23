#coding=utf-8
from flask import Module, render_template, redirect, flash, url_for, g
from flask.ext.login import login_user, logout_user
from models import User
from views.forms import LoginForm


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
            login_user(user, bool(form.remember_me))
            return redirect(url_for('index.home'))
        else:
            msg = '用户名或密码错误，请重新输入'
    return render_template('account/login.html', msg=msg, form = form)


@account.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('index.home'))
