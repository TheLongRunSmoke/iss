from flask import jsonify, request

from app import app
from .basicauth import *
from .statistics import *


@app.route('/api/v1.0/tle', methods=['GET'])
@auth.login_required
def get_tle():
    """
    Main point of API. Extract list of data from database, start from current actual to most recent.
    :return: API data in JSON serialization.
    """
    now = datetime.utcnow()
    stat = Statistics(now)
    authorizer = Auth()
    if authorizer.is_authenticate(auth.username(), request.headers.get('iss-key')):
        query = get_from_db(now.timestamp())

        stat.good_request()
        return jsonify(result)
    else:
        stat.bad_request()
        abort(403)


def get_from_db(timestamp):
    result = {}
    # query = models.TleData.query.filter('timestamp >= ' + str(timestamp)).order_by('timestamp').all()
    query = models.TleData.query.filter('timestamp < ' + str(timestamp)).order_by(models.TleData.timestamp.desc()).first()
    if query is not None:
        try:
            for row in query:
                result[row.timestamp] = row.tle
        except TypeError:
            result[query.timestamp] = query.tle
    return result
