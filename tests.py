import os
import unittest

from app import app, db
from app.models import TleData
from app.tle import get_from_db
from config import basedir

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_tle_query(self):
        tmp = TleData(timestamp=1472550000, tle="some data")
        db.session.add(tmp)
        tmp = TleData(timestamp=1472600000, tle="another data")
        db.session.add(tmp)
        tmp = TleData(timestamp=1472650000, tle="and another data")
        db.session.add(tmp)
        db.session.commit()
        res = get_from_db(1472600200)
        assert len(res) == 1
        print(res)
        assert res == {1472600000: "another data"}


if __name__ == '__main__':
    unittest.main()