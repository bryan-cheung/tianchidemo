try:
    import http.server as BaseHTTPServer 
except:
    import BaseHTTPServer

import os
import shutil
import sys

FILEPATH = "/Users/lizhang/Documents/tianchi/large/trace2.data"

class SimpleHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        with open(FILEPATH, 'rb') as f:
            self.send_response(200)
            self.send_header("Content-Type", 'applicaton/octet-stream')
            self.send_header("Content-Disposition", 'attachment; filename="{}"'.format(os.path.basename(FILEPATH)))
            fs = os.fstat(f.fileno())
            self.send_header("Content-Length", str(fs.st_size))
            self.end_headers()
            shutil.copyfileobj(f, self.wfile)

def test(HandlerClass=SimpleHTTPRequestHandler,
        ServerClass=BaseHTTPServer.HTTPServer,
        protocol="HTTP/1.1"):
    port = 8302
    server_address = ('', port)

    HandlerClass.protocol_version = protocol
    httpd = BaseHTTPServer.HTTPServer(server_address, HandlerClass)

    sa = httpd.socket.getsockname()
    print("Serving HTTP on {0[0]} port {0[1]} ... {1}".format(sa, FILEPATH))
    httpd.serve_forever()

test()

