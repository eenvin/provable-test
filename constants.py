PNT_CONTRACT_ADDRESS = '0x89ab32156e46f46d02ade3fecbe5fc4243b9aaed'
AVERAGE_ETHEREUM_CTIME = 13
EMPTY_STR = ''
NEW_LINE = '\n'
HEADER = {'Content-type': 'application/json'}

url = 'https://aged-wispy-sun.quiknode.pro/a9c866c62d28d63303de21fd44e95f747f725857/'
valid_caching_time = 30


def set_caching_time(t):
    try:
        valid_caching_time = t
        return 1
    except:
        return 0
        raise


def get_caching_time():
    return valid_caching_time


def set_url(u):
    try:
        url = u
        return 1
    except:
        return 0
        raise


def get_url():
    return u
