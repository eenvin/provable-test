import time

from constants import cfg


class Cache:

    # Save cache data into a dictionary
    def __init__(self):
        self.__cache_dict = {}

    def check_cache(self, query):
        if self.__cache_dict.get(query):
            d = self.__cache_dict.get(query)
            if round(time.time()) - d[1] < cfg.get_caching_time():
                print('Data found in cache... \n Data is valid')
                return d[0]
            else:
                print('Data found in cache... \n Data is older than ' + str(cfg.get_caching_time()) + \
                      ' seconds, requesting new data...')
                return None
        else:
            print('Data not found in cache, requesting new data...')
            return None

    def add_cache(self, key, data):
        self.__cache_dict[key] = data


cache = Cache()
