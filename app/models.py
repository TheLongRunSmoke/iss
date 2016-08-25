from app import db

class TleData(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.Integer, index = True, unique = True)
    tle = db.Column(db.String(100))
    addTime = db.Column(db.Integer)

    def __repr__(self):
        return '<Timestamp %r>' % (self.timestamp)

class Stat(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.Integer, index = True, unique = True)
    request = db.Column(db.Integer)
