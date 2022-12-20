def solution(s):
    n = len(s)
    S = sorted(s.count(c) for c in set(s))
    for x in range(int((10**n - 1)**0.5), int((10**(n - 1))**0.5) - 1, -1):
        y = str(x**2)
        Y = sorted(y.count(d) for d in set(y))
        if S == Y:
            return int(y)
    else:
        return -1
