def solution(n, m):
    return 1 if (n & 1) != (m & 1) else solution(n // 2, m // 2) << 1
