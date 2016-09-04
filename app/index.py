import os
from datetime import datetime

from flask import make_response
from flask import render_template
from flask import request
from flask import send_from_directory
from flask_babel import gettext

from app import app, db, babel
from config import LANGUAGES


@app.route('/', methods=['GET', 'POST'])
def index():
    print("index()")
    resp = make_response(render_template("index.html", lang=get_language(), year=get_year()))
    resp = update_cookies(resp)
    return resp


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/dev')
def dev():
    resp = make_response(
        render_template("dev.html", title=gettext("For developers"), lang=get_language(), year=get_year()))
    resp = update_cookies(resp)
    return resp


@app.errorhandler(403)
def not_found_error(error):
    return render_template('403.html', title="403", year=get_year()), 403


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', title="404", year=get_year()), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html', title="500", year=get_year()), 500


@babel.localeselector
def get_locale():
    return get_language()


def get_year():
    now = datetime.utcnow()
    return now.year


def get_language():
    result = "en"
    lang_cookies = request.cookies.get('lang')
    if lang_cookies is None:
        result = request.accept_languages.best_match(LANGUAGES.keys())
    else:
        post = request.form
        if len(post) is 0:
            result = lang_cookies
        else:
            lang_post = post.get('lang', default=None)
            if lang_post is not None:
                result = lang_post
    return result


def update_cookies(resp):
    lang_cookies = request.cookies.get('lang')
    lang_actual = get_language()
    if lang_cookies != lang_actual:
        resp.set_cookie('lang', lang_actual)
    return resp
