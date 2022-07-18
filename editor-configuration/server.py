#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from parseJSON import getFunctionInfo
import json

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(getFunctionInfo(self.path[1:])).encode())

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 80), RequestHandler)
    server.serve_forever()
    
    
    #https://gist.github.com/bsingr/a5ef6834524e82270154a9a72950c842