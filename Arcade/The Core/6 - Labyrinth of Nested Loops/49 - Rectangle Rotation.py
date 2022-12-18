def solution(a, b):

    [m, n] = [int(x / 2**0.5) for x in (a, b)]
    return m*n + (m + 1)*(n + 1) - (m + n)%2
