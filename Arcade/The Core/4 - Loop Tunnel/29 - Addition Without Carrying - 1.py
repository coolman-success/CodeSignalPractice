def solution(param1, param2):

    if param1 < param2:
        param1, param2 = param2, param1
    param1, param2 = str(param1), str(param2)
    param2 = "0"*(len(param1) - len(param2)) + str(param2)
    
    result = [(int(x) + int(y))%10 for x, y in zip(param1, param2)]
    
    return int(''.join([d for d in map(str, result)]))
