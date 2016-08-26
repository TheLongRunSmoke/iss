from app import app, db, models, auth
from flask import jsonify, request
from datetime import datetime

@app.route('/api/v1.0/tle', methods=['GET'])
def get_tle():
    authorizator = auth.Auth()
    result = {}
    if (authorizator.isAuthorized(request.headers.get('iss-key'))):
        now = int(datetime.utcnow().timestamp())
        query = models.TleData.query.filter('timestamp >= ' + str(now)).order_by('timestamp').all()
        if query is not None:
            try:
                for row in query:
                    result[row.timestamp] = row.tle
            except:
                result[query.timestamp] = query.tle
    return jsonify(result)
