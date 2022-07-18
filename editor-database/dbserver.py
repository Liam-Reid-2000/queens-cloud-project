#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from parseCSV import getCSVRecord, writeCSVRecord, genUnique
import json

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        

        # Write to the csv file
        if ("write/" in self.path[1:]):
            recordToWrite = self.path[1:].split('/',2)
            # Generate a reference if none passed
            if (recordToWrite[1] == "genUnique"):
                recordToWrite[1] = genUnique()

            # write the record if reference not exists
            if (writeCSVRecord(recordToWrite[1], recordToWrite[2])):
                self.wfile.write(json.dumps({
                    'error':False,
                    'string':"Saved",
                    'reference':recordToWrite[1]
                }).encode())
            else:
                self.wfile.write(json.dumps({
                    'error':True,
                    'string':"Error: Key already exists"
                }).encode())
            return

        # Get the text about the reference
        respText = getCSVRecord(self.path[1:])
        if (respText == "-1"):
            self.wfile.write(json.dumps({
                'error':True,
                'string':"Error: Not found"
            }).encode())
        else:
            self.wfile.write(json.dumps({
                'error':False,
                'string':str(respText)
            }).encode())
        return

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 80), RequestHandler)
    server.serve_forever()
    
    
    #https://gist.github.com/bsingr/a5ef6834524e82270154a9a72950c842