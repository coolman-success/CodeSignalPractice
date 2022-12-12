def solution(name):
    import re
    return re.match('^[_a-z][a-z0-9_]*$', name, re.IGNORECASE) != None
