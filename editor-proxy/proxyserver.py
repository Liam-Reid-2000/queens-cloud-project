#!/usr/bin/env python31

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from config import getFunctionLinks
import json
import requests

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        
        requestPath = self.path[1 : ]
        pathElements = requestPath.split("/",1)
        key = pathElements[0]
        payload = pathElements[1]
        
        
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        resp = None

        links = getFunctionLinks(pathElements[0])
        for link in links:
            forwardRequestUrl = "http://" + link + ".40231992.qpc.hal.davecutting.uk/" + payload
            resp = requests.get(forwardRequestUrl)
            if (json.loads(resp.content)['error'] == False):
                self.wfile.write(resp.content)
                return
        self.wfile.write(resp.content)
        return
        
    
    
if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 80), RequestHandler)
    server.serve_forever()
    
    
    #https://gist.github.com/bsingr/a5ef6834524e82270154a9a72950c842