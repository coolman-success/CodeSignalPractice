def solution(inputString):
    
    chars = set(inputString)
    return sum(inputString.count(x)%2 != 0 for x in chars) < 2
