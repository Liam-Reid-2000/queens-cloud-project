import json
import requests
import csv
from csv_helper import writeToStatusCSV

payload = "?text=Test%20String%20kayak,"

def checkStatusOK(link):
    try:
        forwardRequestUrl = "http://" + link + ".40231992.qpc.hal.davecutting.uk/" + payload
        resp = requests.get(forwardRequestUrl)
        if (json.loads(resp.content)['error'] == False):
            writeToStatusCSV(link, forwardRequestUrl, True, resp.elapsed.total_seconds())
            return True
        writeToStatusCSV(link, forwardRequestUrl, False, resp.elapsed.total_seconds())
        return False
    except:
        writeToStatusCSV(link, forwardRequestUrl, False, resp.elapsed.total_seconds())
        return False

    
    
    
    