from collections import deque

def solution(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    deque(map(lambda d: d[1].rotate(-d[0]), enumerate(res)), 0)
    return [list(d) for d in res]
