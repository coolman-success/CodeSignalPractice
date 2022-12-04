def solution(inputArray):
    
    res = []
    longest = 0
    
    for word in inputArray:
        if longest < len(word):
            res = [word]
            longest = len(word)
        elif longest == len(word):
            res += [word]
    
    return res
