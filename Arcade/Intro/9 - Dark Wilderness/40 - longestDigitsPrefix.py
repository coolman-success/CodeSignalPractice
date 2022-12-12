def solution(inputString):
    import re
    res = re.search(r'^\d+', inputString)
    return res.group() if res else ""
