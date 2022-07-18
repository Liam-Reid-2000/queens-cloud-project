import unittest
import requests
import subprocess
import time

from http.server import HTTPServer
from proxyserver import RequestHandler

class ProxyServerTest(unittest.TestCase):

    # Test call to server
    def testCommaCountRequest(self):        
        process = subprocess.Popen(["python", "ProxyTestServerRunner.py"])
        time.sleep(1)
        forwardRequestUrl = "http://proxy.40231992.qpc.hal.davecutting.uk/commacount/?text=hello,"
        resp = requests.get(forwardRequestUrl)
        self.assertTrue('{\"error\": false, \"string\": \"There are 1 commas\", \"answer\": 1}' in str(resp.content))
        process.terminate

    def testPalindromeCountRequest(self):        
        process = subprocess.Popen(["python", "ProxyTestServerRunner.py"])
        time.sleep(1)
        forwardRequestUrl = "http://proxy.40231992.qpc.hal.davecutting.uk/palindromecount/?text=kayak,"
        resp = requests.get(forwardRequestUrl)
        self.assertTrue('{\"string\":\"The answer is 1\",\"answer\":1,\"error\":false}' in str(resp.content))
        process.terminate
        
    def testAverageWordLengthRequest(self):        
        process = subprocess.Popen(["python", "ProxyTestServerRunner.py"])
        time.sleep(1)
        forwardRequestUrl = "http://proxy.40231992.qpc.hal.davecutting.uk/averagewordlength/?text=hello,"
        resp = requests.get(forwardRequestUrl)
        self.assertTrue('{\"error\":false,\"string\":\"Average word length: 5\",\"answer\":5}' in str(resp.content))
        process.terminate

    def testVowelCountRequest(self):        
        process = subprocess.Popen(["python", "ProxyTestServerRunner.py"])
        time.sleep(1)
        forwardRequestUrl = "http://proxy.40231992.qpc.hal.davecutting.uk/vowelcount/?text=hello,"
        resp = requests.get(forwardRequestUrl)
        self.assertTrue('{\"error\":false,\"string\":\"Hello from c#\",\"answer\":3}' in str(resp.content))
        process.terminate

    def testFakeServiceRequest(self):        
        process = subprocess.Popen(["python", "ProxyTestServerRunner.py"])
        time.sleep(1)
        forwardRequestUrl = "http://proxy.40231992.qpc.hal.davecutting.uk/fake/?text=hello,"
        resp = requests.get(forwardRequestUrl)
        self.assertTrue('' in str(resp.content))
        process.terminate


if __name__ == '__main__':
    unittest.main()