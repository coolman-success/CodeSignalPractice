def solution(param1, param2):

    res, base = 0, 1
    while param1 > 0 or param2 > 0:
        res += ((param1 + param2) % 10)*base
        base *= 10
        param1, param2 = param1//10, param2//10
    
    return res
