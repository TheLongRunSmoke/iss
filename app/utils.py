from datetime import datetime
from functools import wraps

from flask import make_response
from flask import render_template
from flask import request

from config import LANGUAGES, MAINTENANCE_MODE


def get_year():
    now = datetime.utcnow()
    return now.year


def get_language():
    """
    Determinate language, by request, cookies and POST data.
    :return: language code.
    """
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
    """
    Add cookies to existing response.
    :param resp: response
    :return: response with cookies
    """
    lang_cookies = request.cookies.get('lang')
    lang_actual = get_language()
    if lang_cookies != lang_actual:
        resp.set_cookie('lang', lang_actual)
    return resp


def maintenance(func):
    """
    Decorator. Return maintenance page if needed.
    :return: response.
    """
    @wraps(func)
    def decorated_function():
        if MAINTENANCE_MODE:
            resp = make_response(render_template("maintenance.html", lang=get_language(), year=get_year()))
            resp = update_cookies(resp)
        else:
            resp = func()
        return resp
    return decorated_function


def make_error(page, number):
    resp = make_response(render_template(page, lang=get_language(), title=number, year=get_year()), number)
    resp = update_cookies(resp)
    return resp
