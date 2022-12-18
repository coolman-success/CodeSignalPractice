def solution(inputString):
    import re
    return bool(re.match('^' + ('[\dA-F]{2}-'*6)[:-1] + '$', inputString))
