def solution(n):

    m, k = 1, 1
    while n > k:
        m += 1
        k *= m
    
    return k
