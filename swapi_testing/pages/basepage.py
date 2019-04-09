# This is Main Basic class
# Core functionality will be here

class BaseClass(object):
    def __init__(self):
        self._host = 'https://swapi.co/'
        self._schema = 'api/'
        self._header = {
            'Content-Type': 'application/json'
        }
