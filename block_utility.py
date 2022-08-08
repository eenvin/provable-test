import json

import requests

from constants import url, HEADER


def return_block_time_by_num(num):
    num = hex(num)
    cmd = '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["' + num + '",false],"id":1}'
    data = json.loads(requests.post(url, data=cmd, headers=HEADER).text)
    rt_time = int(data['result']['timestamp'], 16)
    return rt_time
