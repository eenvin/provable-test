from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
import json
import cgi
import time
from datetime import datetime

from cache import add_cache, check_cache
from constants import PNT_CONTRACT_ADDRESS, HEADER, url, EMPTY_STR, NEW_LINE
from interval_detection import find_block_interval


class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    # def do_HEAD(self):
    #     self._set_headers()

    # POST echoes the message adding a JSON field
    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.get('content-type'))

        # refuse to receive non-json content
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return

        # read the message and convert it into a python dictionary
        length = int(self.headers.get('content-length'))
        try:
            str_in = self.rfile.read(length).decode()
            message = json.loads(str_in)
        except:
            if str_in.find("\"") == -1:
                err = "No \" character found in input string. This server do not support \" character in input " \
                      "stream if not escaped. Please escape all \" characters "
                self._set_headers()
                self.wfile.write(err.encode("utf-8"))
                return
            else:
                return

        # Check cache
        cached = check_cache(str(message))
        if cached is not None:
            self._set_headers()
            self.wfile.write(str(cached).encode("utf-8"))
            return

        # add a property to the object, just to mess with data
        address = message['address']
        try:
            start_time = int(message['from'])
            end_time = int(message['to'])
        except:
            str_out = "Start time or End time data is not valid, please insert Unix timestamp format"
            self._set_headers()
            self.wfile.write(str_out.encode("utf-8"))
            raise

        # get all transaction
        response = tr_num_byaddr(address, start_time, end_time)
        if response:
            rsp_str = EMPTY_STR
            for rsp in response:
                # response_j = json.loads(''.join(rsp))
                # data = [response_j, round(time.time())]
                # add_cache(str(message), data)
                rsp_str = rsp_str + EMPTY_STR.join(rsp) + NEW_LINE

            data = [rsp_str, round(time.time())]
            add_cache(str(message), data)
            # send the message back
            self._set_headers()
            self.wfile.write(rsp_str.encode("utf-8"))
        else:
            response = 'No transaction found'
            self._set_headers()
            self.wfile.write(response.encode("utf-8"))


def tr_num_byaddr(addr, start_time, end_time):
    r_list = []
    start, end = find_block_interval(start_time, end_time)
    cmd = '{"jsonrpc": "2.0","id": 1,"method": "eth_getLogs","params": [{"fromBlock": "' + hex(
        start) + '","toBlock": "' + hex(end) + '","address": "' + PNT_CONTRACT_ADDRESS + '"}]}'
    data = json.loads(requests.post(url, data=cmd, headers=HEADER).text)
    d = data['result']
    readable_start = datetime.fromtimestamp(start_time)
    readable_end = datetime.fromtimestamp(end_time)
    print('Searching transactions from/to addr {0} between {1} and {2}'.format(str(addr), str(readable_start),
                                                                               str(readable_end)))
    for index in range(len(d)):
        din = d[index]
        tpcs = din['topics']
        try:
            sender = hex(int(tpcs[2], 16))
            receiver = hex(int(tpcs[3], 16))
        except:
            sender = 0
            receiver = 0
        if sender == addr or receiver == addr:
            txid = din['transactionHash']
            amount = str(int(din['data'][:66], 16))
            result = '{"txid":"' + txid + '","sender":"' + sender + '","receiver":"' + receiver + '","amount":"' \
                     + amount + '"}'
            print('Found transaction: ' + result)
            r_list.append(result)
    return r_list


def run(server_class=HTTPServer, handler_class=Server, port=3000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)

    print('Starting httpd on port %d...' % port)
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
