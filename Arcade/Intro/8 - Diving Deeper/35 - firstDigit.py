def solution(inputString):
    import re
    m = re.search(r'\d', inputString)
    return m.group()