from hashlib import md5

from flask import abort
from flask_httpauth import HTTPBasicAuth

from .clients import CLIENTS
from .statistics import *

# clients.py must contain dictionary named CLIENTS look like this:
# CLIENTS = {
#    "<login>" : {"password": "<password md5 hash>", "keys": ["0000"]}
# }

auth = HTTPBasicAuth()


@auth.get_password
def get_password(username):
    if username is not None:
        if username in CLIENTS.keys():
            user = CLIENTS[username]
            return user["password"]
    return None


@auth.error_handler
def unauthorized():
    nowdt = datetime.utcnow()
    stat = Statistics(nowdt)
    stat.bad_request()
    abort(403)


@auth.hash_password
def hash_pw(password):
    return md5(password.encode('utf-8')).hexdigest()


class Auth:
    """
    Check user authenticate.
    May be more complex, so define in separated class.
    """

    @staticmethod
    def is_authenticate(login, key):
        """
        Validate key given in request.
        :param login: user login.
        :param key: request key.
        :return: True if key exist, False otherwise.
        """
        for client in CLIENTS[login]["keys"]:
            if key == client:
                return True
        return False
