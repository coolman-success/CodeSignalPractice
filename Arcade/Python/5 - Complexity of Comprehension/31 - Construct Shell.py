def solution(n):
    return [[0] * i if i <= n else [0] * (2*n - i) for i in range(1, 2*n)]
