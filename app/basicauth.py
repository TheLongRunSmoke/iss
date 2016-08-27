from .clients import CLIENTS
from flask_httpauth import HTTPBasicAuth
from flask import abort
from hashlib import md5
from .statistics import *
from datetime import datetime
# clients.py must containe dictonary named CLIENTS look like this:
#CLIENTS = {
#    "<login>" : {"password": "<password md5 hash>", "keys": ["0000"]}
#}

auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username != None:
        if username in CLIENTS.keys():
            user = CLIENTS[username]
            return user["password"]
    return None

@auth.error_handler
def unauthorized():
    nowdt = datetime.utcnow()
    stat = Statistics(nowdt)
    stat.badRequest()
    abort(403)

@auth.hash_password
def hash_pw(username,password):
    return md5(password.encode('utf-8')).hexdigest()

class Auth():
    """docstring for ."""
    def isAuthorized(self,login,key):
        for client in CLIENTS[login]["keys"]:
            if (key == client):
                return True
        return False
