import json
from collections import OrderedDict

def solution(jsonFile):
    return json.dumps(clean(json.loads(jsonFile, object_pairs_hook=OrderedDict)))
        
def clean(x):
    if type(x) is int or type(x) is float:
        return 0
    elif type(x) is str:
        return ""
    elif type(x) is list:
        return []
    elif type(x) is OrderedDict:
        res = OrderedDict()
        for k, v in x.items():
            res[k] = clean(v)
        return res
