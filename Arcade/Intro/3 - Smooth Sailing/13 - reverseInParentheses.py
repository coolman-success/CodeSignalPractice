def solution(inputString):
    
    for i, ch in enumerate(inputString):
        if ch == '(':
            s = i
        if ch == ')':
            e = i
            return solution(inputString[:s] + inputString[s+1:e][::-1] + inputString[e+1:])
    
    return inputString
