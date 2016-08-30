import os
from datetime import datetime

from flask import render_template
from flask import send_from_directory

from app import app, db


@app.route('/')
def index():
    return render_template("index.html", year=get_year())


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/dev')
def dev():
    return render_template("dev.html", title="Разработчикам", year=get_year())


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


def get_year():
    now = datetime.utcnow()
    return now.year
