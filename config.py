import os
from jobs import gettlefromproviders

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

JOBS = [
    {
        'id': 'job1',
        'func': 'jobs.gettlefromproviders:run',
        'args': (),
        'trigger': 'interval',
        'days': 1
    }
]

MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None
# administrator list
ADMINS = ['thelongrunsmoke@gmail.com']
