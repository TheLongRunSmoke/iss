from .clients import CLIENTS
# clients.py must containe list named CLIENTS with access keys.  

class Auth():
    """docstring for ."""
    def isAuthorized(self,key):
        for client in CLIENTS:
            if (key == client):
                return True
        return False
