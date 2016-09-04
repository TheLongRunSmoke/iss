import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_RECORD_QUERIES = True
DATABASE_QUERY_TIMEOUT = 0.5

JOBS = [
    {
        'id': 'job1',
        'func': 'jobs.get_tle_from_providers:run',
        'args': (),
        'trigger': 'interval',
        'days': 1
    }
]

MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None
# administrator email list.
ADMINS = ['thelongrunsmoke@gmail.com']
LANGUAGES = {
    'en': 'English',
    'ru': 'Русский'
}

MAINTENANCE_MODE = False
