def solution(a, b):
    
    diff = []
    for x, y in zip(a, b):
        if x != y:
            diff.append([x, y])
            if len(diff) > 2:
                return False
    
    if len(diff) == 0 or len(diff) == 2 and diff[0] == diff[1][::-1]:
        return True
    
    return False
