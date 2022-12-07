def solution(n):

    base = 1
    while n > 9:
        n = (n + 5) // 10
        base *= 10
    
    return n*base
