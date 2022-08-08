import json

import requests

from block_utility import return_block_time_by_num
from constants import url, HEADER, AVERAGE_ETHEREUM_CTIME


def find_block_interval(start_time, end_time):
    # get latest block number and timestamp
    cmd = '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["latest",false],"id":1}'
    data = json.loads(requests.post(url, data=cmd, headers=HEADER).text)
    l_num = int(data['result']['number'], 16)
    l_time = int(data['result']['timestamp'], 16)

    # START BLOCK
    print('Searching start block...')
    # every ~thirteen second a block is mined -> estimate first block inside time interval
    if l_time - start_time <= 0:
        start = l_num
    else:
        blk_ago = round((l_time - start_time) / AVERAGE_ETHEREUM_CTIME)
        find_blk = l_num - blk_ago
        t = return_block_time_by_num(find_blk)

        blk_ago = round(abs(start_time - t) / AVERAGE_ETHEREUM_CTIME)
        if start_time - t > 0:
            find_blk = find_blk + blk_ago
        else:
            find_blk = find_blk - blk_ago
        t = return_block_time_by_num(find_blk)

        blk_ago = round(abs(start_time - t) / AVERAGE_ETHEREUM_CTIME)
        if start_time - t > 0:
            find_blk = find_blk + blk_ago
        else:
            find_blk = find_blk - blk_ago
        t = return_block_time_by_num(find_blk)

        if start_time - t > 0:
            while start_time - t > 0:
                find_blk = find_blk + 1
                t = return_block_time_by_num(find_blk)
            start = find_blk + 1
        else:
            while start_time - t <= 0:
                find_blk = find_blk - 1
                t = return_block_time_by_num(find_blk)
            start = find_blk
    print('Start block found: ' + str(start))

    # END BLOCK
    print('Searching end block...')
    # every ~thirteen second a block is mined -> estimate first block inside time interval
    if l_time - end_time <= 0:
        end = 0
    else:
        blk_ago = round((l_time - end_time) / AVERAGE_ETHEREUM_CTIME)
        find_blk = l_num - blk_ago
        t = return_block_time_by_num(find_blk)

        blk_ago = round(abs(end_time - t) / AVERAGE_ETHEREUM_CTIME)
        if end_time - t > 0:
            find_blk = find_blk + blk_ago
        else:
            find_blk = find_blk - blk_ago
        t = return_block_time_by_num(find_blk)

        blk_ago = round(abs(end_time - t) / AVERAGE_ETHEREUM_CTIME)
        if end_time - t > 0:
            find_blk = find_blk + blk_ago
        else:
            find_blk = find_blk - blk_ago
        t = return_block_time_by_num(find_blk)

        if end_time - t > 0:
            while end_time - t > 0:
                find_blk = find_blk + 1
                t = return_block_time_by_num(find_blk)
            end = find_blk + 1
        else:
            while end_time - t <= 0:
                find_blk = find_blk - 1
                t = return_block_time_by_num(find_blk)
            end = find_blk
    print('End block found: ' + str(end))

    return start, end