# -*- coding: utf-8 -*-
#!/usr/bin/python3

from mitmproxy.options import Options
from mitmproxy.proxy.config import ProxyConfig
from mitmproxy.proxy.server import ProxyServer
from mitmproxy.tools.dump import DumpMaster

import argparse

GOOGLE_URL = 'googleapis.com'

class Addon(object):

    def __init__(self, token):
        super().__init__()
        self.token = token
    
    def request(self, flow):
        '''
        Simple search and replace of the token in the HTTP request
        '''

        if GOOGLE_URL in flow.request.pretty_url:
            # print(flow.request.pretty_url)
            # print(flow.request.headers)
            if 'oauth2' not in flow.request.pretty_url:
                flow.request.headers['authorization'] = 'Bearer %s' % self.token

			
class ProxyMaster(DumpMaster):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        try:
            DumpMaster.run(self)
        except KeyboardInterrupt:
            self.shutdown()

if __name__ == "__main__":

    # Parse args
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", type=str, help="Auth token")
    parser.add_argument("--port", type=str, help="Port to listen to")
    args = parser.parse_args()

    # Set options
    options = Options(
        listen_host='0.0.0.0', 
        listen_port=int(args.port), 
        http2=True
    )
    config = ProxyConfig(options)

    # Create master
    master = ProxyMaster(options, with_termlog=False, with_dumper=False)
    master.server = ProxyServer(config)
    master.addons.add(Addon(args.token))

    # Run the proxy
    master.run()