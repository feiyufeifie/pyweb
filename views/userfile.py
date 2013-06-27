#coding=utf-8
from flask import Module, render_template, redirect, url_for, request
from extensions import file_set
from views.forms import UploadFileForm


userfile = Module(__name__)


@userfile.route('/list')
def list():
    return render_template('userfile/list.html')


@userfile.route('/upload', methods=['GET', 'POST'])
def upload():
    msg = None
    form = UploadFileForm()
    if form.validate_on_submit():
        try:
            file = form.file.data
            file_set.save(file)
            return redirect(url_for('userfile.list'))
        except Exception as e:
            msg = '上传失败，请检查文件格式'
    return render_template('userfile/uplaod.html',msg=msg, form=form)