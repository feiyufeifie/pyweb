#coding=utf-8
from flask import Module, render_template, redirect, url_for, request, g
from flask.ext.login import login_required
from extensions import file_set
from models import UserFile
from views.forms import UploadFileForm


userfile = Module(__name__)


@userfile.route('/list')
@login_required
def list():
    file_list = UserFile.find_by_userid(g.user.id)
    return render_template('userfile/list.html', list=file_list)


@userfile.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    msg = None
    form = UploadFileForm()
    if form.validate_on_submit():
        try:
            file = form.file.data
            file_name = file_set.save(file)
            UserFile.add(g.user.id, file_name)
            return redirect(url_for('userfile.list'))
        except Exception as e:
            msg = '上传失败，请检查文件格式'
    return render_template('userfile/uplaod.html',msg=msg, form=form)