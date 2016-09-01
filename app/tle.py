from flask import jsonify, request
from flask.ext.sqlalchemy import get_debug_queries

from app import app
from config import DATABASE_QUERY_TIMEOUT
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
        result = get_from_db(now.timestamp())
        stat.good_request()
        return jsonify(result)
    else:
        stat.bad_request()
        abort(403)


def get_from_db(timestamp):
    result = {}
    # TODO: think about optimization for this
    actual = models.TleData.query.filter(models.TleData.timestamp < str(timestamp)) \
        .order_by(models.TleData.timestamp.desc()).first()
    query = models.TleData.query.filter(models.TleData.timestamp >= actual.timestamp) \
        .order_by(models.TleData.timestamp.asc()).all()
    if query is not None:
        try:
            for row in query:
                result[row.timestamp] = row.tle
        except TypeError:
            result[query.timestamp] = query.tle
    return result


@app.after_request
def after_request(response):
    for query in get_debug_queries():
        if query.duration >= DATABASE_QUERY_TIMEOUT:
            app.logger.warning("SLOW QUERY: %s\nParameters: %s\nDuration: %fs\nContext: %s\n" % (
                query.statement, query.parameters, query.duration, query.context))
    return response
