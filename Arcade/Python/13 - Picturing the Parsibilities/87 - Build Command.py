def solution(jsonFile):
    import json
    def init(jsonObj):
        res = {}
        for key, value in jsonObj.items():
            t = type(value)
            if t == str:
                res[key] = ""
            elif t == list:
                res[key] = []
            elif t in [int, float]:
                res[key] = 0
            elif t == dict:
                res[key] = init(value)
        return res
    
    temp = json.loads(jsonFile)
    return json.dumps(init(temp))
