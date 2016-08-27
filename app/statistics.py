from app import app, db, models
from datetime import datetime,timezone

class Statistics(object):

    def __init__(self, now):
        super(Statistics, self).__init__()
        self.timestamp = int(datetime(now.year, now.month, now.day, now.hour, tzinfo=timezone.utc).timestamp())

    def goodRequest(self):
        query = models.Stat.query.filter_by(timestamp=self.timestamp).first()
        if query is None:
            row = models.Stat(timestamp=self.timestamp, request=1, badrequest=0)
            db.session.add(row)
            db.session.commit()
        else:
            count = query.request + 1
            query.request = count
            db.session.commit()

    def badRequest(self):
        query = models.Stat.query.filter_by(timestamp=self.timestamp).first()
        if query is None:
            row = models.Stat(timestamp=self.timestamp, request=0, badrequest=1)
            db.session.add(row)
            db.session.commit()
        else:
            count = query.badrequest + 1
            query.badrequest = count
            db.session.commit()
