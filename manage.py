#coding=utf-8
from flask.ext.script import Manager, Server, prompt_bool
from extensions import db
from pyweb import create_app

manager = Manager(create_app('config'))

manager.add_command("runserver", Server('0.0.0.0', port=8080))


@manager.command
def createall():
    db.create_all()


@manager.command
def dropall():
    if prompt_bool("Are you sure ? You will lose all your data !"):
        db.drop_all()


if __name__ == "__main__":
    manager.run()