import requests
import json


def getFunctionConfig(key):
    forwardRequestUrl = "http://config.40231992.qpc.hal.davecutting.uk/" + key
    functionConfig = json.loads(requests.get(forwardRequestUrl).content)
    return functionConfig


def getFunctionLinks(key):
    functionConfig = getFunctionConfig(key)
    links = []
    links.append(functionConfig['link1'])
    links.append(functionConfig['link2'])
    links.append(functionConfig['link3'])
    return links