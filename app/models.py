from app import db

class TleData(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.Integer, index = True, unique = True)
    tle = db.Column(db.String(100))
    addTime = db.Column(db.Integer)

    def __repr__(self):
        return 'From: %r\nISS\n%r\n' % (self.timestamp, self.tle)

    def str(self):
        return 'From: %r\nISS\n%r\n' % (self.timestamp, self.tle)

class Stat(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.Integer, index = True, unique = True)
    request = db.Column(db.Integer)
    badrequest = db.Column(db.Integer)

    def __repr__(self):
        return 'From: %r : %r : %r' % (self.timestamp, self.request, self.badrequest)
