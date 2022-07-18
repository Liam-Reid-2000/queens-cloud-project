import json

def getFunctionInfo(key):
    with open('functionlinks.json') as f:
        data = json.load(f)
    if (key == "all"):
        return data
    else:
        for func in data['Functions']:
            if (func['key'] == key):
                return func

    