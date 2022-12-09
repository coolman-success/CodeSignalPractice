def solution(a, b):
    
    diff = []
    for x, y in zip(a, b):
        if x != y:
            diff += [(x, y)]
            if len(diff) > 2:
                return False
    if len(diff) == 1:
        return False
    if len(diff) == 2:
        if set(diff[0]) == set(diff[1]):
            return True
        else:
            return False
    return True
