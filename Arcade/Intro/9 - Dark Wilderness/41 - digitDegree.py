def solution(n):

    degree = 0
    while n > 9:
        n = sum(int(d) for d in str(n))
        degree += 1
    return degree