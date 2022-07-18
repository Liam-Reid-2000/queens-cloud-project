import requests
import json


def getFunctionConfig(key):
    forwardRequestUrl = "http://config.40231992.qpc.hal.davecutting.uk/" + key
    functionConfig = json.loads(requests.get(forwardRequestUrl).content)
    return functionConfig