def solution(inputArray):
    
    res = {}
    
    for word in inputArray:
        res[len(word)] = res[len(word)] + [word] if len(word) in res else [word]
    
    return res[max(res)]
