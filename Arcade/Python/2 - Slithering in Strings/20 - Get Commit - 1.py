def solution(commit):
    import re
    return re.sub('^[0+!?]*', '', commit, 1)
