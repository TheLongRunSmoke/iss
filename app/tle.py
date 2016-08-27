from app import app, db, models
from .basicauth import *
from flask import jsonify, request
from datetime import datetime

@app.route('/api/v1.0/tle', methods=['GET'])
@auth.login_required
def get_tle():
    authorizator = Auth()
    result = {}
    if (authorizator.isAuthorized(auth.username(), request.headers.get('iss-key'))):
        now = int(datetime.utcnow().timestamp())
        query = models.TleData.query.filter('timestamp >= ' + str(now)).order_by('timestamp').all()
        if query is not None:
            try:
                for row in query:
                    result[row.timestamp] = row.tle
            except:
                result[query.timestamp] = query.tle
        return jsonify(result)
    else:
        abort(403)
