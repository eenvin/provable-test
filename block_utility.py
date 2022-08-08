import json

import requests

from constants import HEADER, cfg


def return_block_time_by_num(num):
    num = hex(num)
    cmd = '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["' + num + '",false],"id":1}'
    data = json.loads(requests.post(cfg.get_url(), data=cmd, headers=HEADER).text)
    rt_time = int(data['result']['timestamp'], 16)
    return rt_time


def test_node(url):
    cmd = '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":83}'
    if requests.post(cfg.get_url(), data=cmd, headers=HEADER):
        return True
    else:
        return False
