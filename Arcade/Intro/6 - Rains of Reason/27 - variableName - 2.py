def solution(name):
    import re
    return re.match('^[_a-zA-Z][a-zA-Z0-9_]*$', name) != None
