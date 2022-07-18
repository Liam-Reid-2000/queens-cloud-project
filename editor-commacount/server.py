#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json
from commaCount import countCommas

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        commas = countCommas(self.path.replace("/?text=",""))
        if (commas == -1):
            self.wfile.write(json.dumps({
                'error':True,
                'string':"Error: Invalid or Empty string",
                'answer':0
            }).encode())
        else:
            self.wfile.write(json.dumps({
                'error':False,
                'string':"There are " + str(commas) + " commas",
                'answer':commas
            }).encode())
        return

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 80), RequestHandler)
    server.serve_forever()
    
    
    #https://gist.github.com/bsingr/a5ef6834524e82270154a9a72950c842