PNT_CONTRACT_ADDRESS = '0x89ab32156e46f46d02ade3fecbe5fc4243b9aaed'
AVERAGE_ETHEREUM_CTIME = 13
EMPTY_STR = ''
NEW_LINE = '\n'
HEADER = {'Content-type': 'application/json'}


class Config:

    def __init__(self):
        self._url = 'https://aged-wispy-sun.quiknode.pro/a9c866c62d28d63303de21fd44e95f747f725857/'
        self._valid_caching_time = 30
        self._port = 3000

    def set_port(self, p):
        try:
            self._port = p
            return 1
        except:
            return 0
            raise

    def get_port(self):
        return self._port

    def set_caching_time(self, t):
        try:
            self._valid_caching_time = t
            return 1
        except:
            return 0
            raise

    def get_caching_time(self):
        return self._valid_caching_time

    def set_url(self, u):
        try:
            self._url = u
            return 1
        except:
            return 0
            raise

    def get_url(self):
        return self._url


cfg = Config()
