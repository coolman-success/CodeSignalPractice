def solution(inputString):
    import re
    return bool(re.match('^' + '-'.join(['[0-9A-F][0-9A-F]']*6) + '$', inputString))
