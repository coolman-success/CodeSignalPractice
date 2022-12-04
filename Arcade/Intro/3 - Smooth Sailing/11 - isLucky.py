def solution(n):
    
    digits = list(map(int, str(n)))
    center = len(digits)//2
    
    return sum(digits[:center]) == sum(digits[center:])
