from datetime import datetime, timezone

from app import db, models


class Statistics(object):
    """
    Class contain methods for counting requests.
    """

    def __init__(self, now):
        super(Statistics, self).__init__()
        # get timestamp for current hour in UTC+0 timezone
        self.timestamp = int(datetime(now.year, now.month, now.day, now.hour, tzinfo=timezone.utc).timestamp())

    def good_request(self):
        """
        Count one "good" request - authorized and passed by key.
        Find or create row for current hour in database, then increase value.
        """
        query = models.Stat.query.filter_by(timestamp=self.timestamp).first()
        if query is None:
            row = models.Stat(timestamp=self.timestamp, request=1, badrequest=0)
            db.session.add(row)
            db.session.commit()
        else:
            count = query.request + 1
            query.request = count
            db.session.commit()

    def bad_request(self):
        """
        Count request there has not been authorizer or authenticated.
        """
        query = models.Stat.query.filter_by(timestamp=self.timestamp).first()
        if query is None:
            row = models.Stat(timestamp=self.timestamp, request=0, badrequest=1)
            db.session.add(row)
            db.session.commit()
        else:
            count = query.badrequest + 1
            query.badrequest = count
            db.session.commit()
