#coding=utf-8
import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask, request, redirect, render_template, url_for, g
from flask.ext.principal import Principal, identity_loaded
from models import User
import views
from extensions import *

import pymysql
pymysql.install_as_MySQLdb()

DEFAULT_APP_NAME = 'pyweb'

DEFAULT_MODULES = (
    (views.account, "/account"),
)


def create_app(config=None, modules=None):
    if modules is None:
        modules = DEFAULT_MODULES

    app = Flask(DEFAULT_APP_NAME)

    # config
    app.config.from_pyfile(config)

    configure_extensions(app)

    configure_identity(app)
    configure_logging(app)
    configure_errorhandlers(app)
    configure_before_handlers(app)
    # configure_template_filters(app)
    # configure_context_processors(app)
    # configure_uploads(app, (photos,))
    #
    # configure_i18n(app)

    # register module
    configure_modules(app, modules)
    return app


def configure_extensions(app):
    db.init_app(app)
    mail.init_app(app)


def configure_identity(app):
    principal = Principal(app)

    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        g.user = User.query.from_identity(identity)


def configure_before_handlers(app):
    @app.before_request
    def authenticate():
        g.user = getattr(g.identity, 'user', None)


def configure_errorhandlers(app):
    @app.errorhandler(401)
    def unauthorized(error):
        return redirect(url_for("account.login", next=request.path))

    @app.errorhandler(403)
    def forbidden(error):
        return render_template("errors/403.html", error=error)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/404.html", error=error)

    @app.errorhandler(500)
    def server_error(error):
        return render_template("errors/500.html", error=error)


def configure_modules(app, modules):
    for module, url_prefix in modules:
        app.register_module(module, url_prefix=url_prefix)


def configure_logging(app):
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s ''[in %(pathname)s:%(lineno)d]')

    debug_log = os.path.join(app.root_path, app.config['DEBUG_LOG'])

    debug_file_handler = RotatingFileHandler(debug_log, maxBytes=100000, backupCount=10)

    debug_file_handler.setLevel(logging.DEBUG)
    debug_file_handler.setFormatter(formatter)
    app.logger.addHandler(debug_file_handler)

    error_log = os.path.join(app.root_path, app.config['ERROR_LOG'])

    error_file_handler = \
        RotatingFileHandler(error_log, maxBytes=100000, backupCount=10)

    error_file_handler.setLevel(logging.ERROR)
    error_file_handler.setFormatter(formatter)
    app.logger.addHandler(error_file_handler)


if __name__ == '__main__':
    create_app('config.cfg').run()
