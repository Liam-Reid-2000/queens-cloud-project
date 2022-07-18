import unittest
import requests
import subprocess
import time

from http.server import HTTPServer
from commaCount import countCommas
from server import RequestHandler

class CountCommasTest(unittest.TestCase):

    # Test method
    def test_upper(self):
        self.assertEqual(1, countCommas("Cloud, Project"))
        self.assertEqual(4, countCommas(",Cloud, ,Project,"))
        self.assertEqual(2, countCommas(",,"))
        self.assertEqual(0, countCommas("Cloud Project"))
        self.assertEqual(-1, countCommas(""))

    # Test call to server
    def testHandler(self):        
        process = subprocess.Popen(["python", "commaCountServerTest.py"])
        time.sleep(1)
        forwardRequestUrl = "http://localhost:8080/?text=hello, how are you"
        resp = requests.get(forwardRequestUrl)
        self.assertTrue('{\"error\": false, \"string\": \"There are 1 commas\", \"answer\": 1}' in str(resp.content))
        process.terminate


if __name__ == '__main__':
    unittest.main()