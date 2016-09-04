import os

from flask import send_from_directory
from flask_babel import gettext

from app import app, db, babel
from .utils import *


@app.route('/', methods=['GET', 'POST'])
@maintenance
def index():
    resp = make_response(render_template("index.html", lang=get_language(), year=get_year()))
    resp = update_cookies(resp)
    return resp


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/dev')
@maintenance
def dev():
    resp = make_response(
        render_template("dev.html", title=gettext("For developers"), lang=get_language(), year=get_year()))
    resp = update_cookies(resp)
    return resp


@app.errorhandler(403)
def not_found_error(error):
    return make_error('403.html', 403)


@app.errorhandler(404)
def not_found_error(error):
    return make_error('404.html', 404)


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return make_error('500.html', 500)


@babel.localeselector
def get_locale():
    return get_language()
