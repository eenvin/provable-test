import time

from constants import get_caching_time

# Save cache data into a dictionary -- not productive, unsecure data handling
cache_dict = {}


def check_cache(query):
    if cache_dict.get(query):
        d = cache_dict.get(query)
        if round(time.time()) - d[1] < get_caching_time():
            print('Data found in cache... \n Data is valid')
            return d[0]
        else:
            print('Data found in cache... \n Data is older than ' + str(get_caching_time()) + 'seconds, requesting '
                                                                                              'new data...')
            return None
    else:
        print('Data not found in cache, requesting new data...')
        return None


def add_cache(key, data):
    cache_dict[key] = data
