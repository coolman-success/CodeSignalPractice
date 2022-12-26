from collections import deque

def solution(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    deque(map(lambda d, i: d.rotate(-i), res, range(n)), 0)
    return [list(d) for d in res]
