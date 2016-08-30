from datetime import datetime

import app
from .crawler import TleCrawler


def run():
    """
    Run crawler process.
    """
    crawler = TleCrawler()
    if crawler.status == 0:
        data = crawler.get_data()
        write_to_db(data)
        now = datetime.utcnow().date()
        query = app.models.TleData.query.filter_by(addTime=int(datetime(now.year, now.month, now.day).timestamp())).all()
        if query is not None:
            with app.app.app_context():
                app.mailer.Mailer.new_tle_notify(query)
    else:
        with app.app.app_context():
            app.mailer.Mailer.tle_provider_fail_notify()


def write_to_db(data):
    """
    Save TLE to database. Create or update rows as needed.
    :param data: list of TLE, contain list with TLE strings and timestamp for them.
    """
    now = datetime.utcnow().date()
    timestamp = int(datetime(now.year, now.month, now.day).timestamp())
    for tle in data:
        query = app.models.TleData.query.filter_by(timestamp=tle[0]).first()
        if query is None:
            row = app.models.TleData(timestamp=tle[0], tle=tle[1], addTime=timestamp)
            app.db.session.add(row)
            app.db.session.commit()
        else:
            if query.tle != tle[1]:
                query.tle = tle[1]
                query.addTime = timestamp
                app.db.session.commit()
