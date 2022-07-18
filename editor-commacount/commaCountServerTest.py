#!/usr/bin/env python3

from http.server import HTTPServer
from server import RequestHandler



if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), RequestHandler)
    server.serve_forever()
    
    