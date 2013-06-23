#coding=utf-8
from flask import Module, render_template, g
from flask.ext.login import login_required

index = Module(__name__)


@index.route('/')
@index.route('/index')
@login_required
def home():
    user = g.user
    return render_template('index.html', user=user)