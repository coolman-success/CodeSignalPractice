def solution(inputString):
    import re
    match = re.findall(r'\d+', inputString)
    return sum(int(found) for found in match)
