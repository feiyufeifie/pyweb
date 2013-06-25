#coding=utf-8
from flask import Module, render_template, redirect, flash, url_for, g, request
from flask.ext.login import login_user, logout_user
from utils import MailUtil, EncryptionUtil
from models import User
from views.forms import RegForm, LoginForm, FindPwdForm, ResetPwdForm


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
            token = EncryptionUtil.encrypt(str(user.id) + '#' + str(user.email))
            mailbody = '''
            要重设您的  帐户 {0} 的密码，请点击以下链接：<br/>
            <a>http://127.0.0.1:5000/account/resetpwd/{1}<a/> <br/>
            如果点击以上链接没有反应，请将该网址复制并粘贴到新的浏览器窗口中。'''
            MailUtil.send_mail('找回密码', mailbody.format(email, token), email)
        else:
            msg = '该邮箱没有注册，请核对信息'

    return render_template('account/findpwd.html', msg=msg, email=email, user=user, form=form)


@account.route('/resetpwd/<token>',  methods=['GET', 'POST'])
@account.route('/resetpwd',  methods=['GET', 'POST'])
def resetpwd(token=''):
    msg = None
    form = ResetPwdForm()
    if token != '':
            form.token.data = token

    if not form.token.data:
        return redirect(url_for('index.home'))

    token_str = str(form.token.data)
    user = None
    try:
        data = EncryptionUtil.decrypt(token_str).split('#')
        user = User.get_by_id(data[0])
        if user.email != data[1]:
            return redirect(url_for('index.home'))
    except Exception as e:
        return redirect(url_for('index.home'))

    if form.validate_on_submit():
        if user and form.pwd.data:
            user.pwd = str(form.pwd.data)
            User.update(user)
            login_user(user)
            return redirect(url_for('index.home'))

    return render_template('account/resetpwd.html', form=form)