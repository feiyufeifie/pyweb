#coding=utf-8
from flask import Module, render_template


account = Module(__name__)


@account.route('/login')
def login():
    return render_template('account/login.html')