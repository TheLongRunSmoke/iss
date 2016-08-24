from app import db

class TleData(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.Integer, index = True, unique = True)
    first = db.Column(db.String(100))
    second = db.Column(db.String(100))
    useCount = db.Column(db.Integer)

    def __repr__(self):
        return '<Timestamp %r>' % (self.timestamp)
