from collections import deque

def solution(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    deque(map(lambda i: res[i].rotate(-i), range(n)), 0)
    return [list(d) for d in res]
