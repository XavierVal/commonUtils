__author__ = 'x'

import json
import requests
from requests.exceptions import RequestException

class SendUtils(object):
    def __init__(self,
                 method,
                 instance="127.0.0.1",
                 port="999",
                 headers={"Accept": "application/json", 'content-type': 'application/json'}):
        self.headers = headers
        self.instance = instance
        self.port = port
        self.endpoint = 'http://' + instance + ':' + port


        def send_request(self, method='GET', url=self.endpoint, headers=self.headers, payload=None, verify=None, query=None):
            parameters = {
                'method': method,
                'url': url,
            }

            if headers is not None:
                parameters.update({'headers': headers})

            if payload is not None:
                try:
                    parameters.update({'data': json.dumps(payload)})
                except ValueError:
                    parameters.update({'data': payload})

            if query is not None:
                parameters.update({'params': query})

            if verify is not None:
                parameters.update({'verify': verify})

            # Send the requests
            try:
                response = requests.request(**parameters)
            except RequestException, e:
                assert False, 'ERROR: [NETWORK ERROR] {}'.format(e)

            print response
            return response
