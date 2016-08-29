from app import app
from flask import render_template
import os
from flask import send_from_directory
from datetime import datetime

@app.route('/')
def index():
    return render_template("index.html", year=getYear())

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/dev')
def dev():
    return render_template("dev.html", title="Разработчикам", year=getYear())

@app.errorhandler(403)
def not_found_error(error):
    return render_template('403.html', title="403", year=getYear()), 403

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', title="404", year=getYear()), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html', title="500", year=getYear()), 500

def getYear():
    now = datetime.utcnow()
    return now.year
