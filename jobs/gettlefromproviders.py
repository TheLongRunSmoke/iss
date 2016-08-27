import app
from .tlecrawler import TleCrawler
from datetime import datetime

def run():
    crawler = TleCrawler()
    if crawler.status == 0:
        data = crawler.getData()
        writeToDB(data)
        now = datetime.utcnow().date()
        query = app.models.TleData.query.filter_by(addTime=int(datetime(now.year, now.month, now.day).timestamp())).all()
        if query is not None:
            with app.app.app_context():
                app.mailer.Mailer.newTleNotification('\n'.join(str(x) for x in query))
    else:
        with app.app.app_context():
            app.mailer.Mailer.tleProviderFail()

def writeToDB(data):
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
