import os
from jobs import get_tle_from_providers

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

JOBS = [
    {
        'id': 'job1',
        'func': 'jobs.get_tle_from_providers:run',
        'args': (),
        'trigger': 'interval',
        'seconds': 15
    }
]
