def solution(s):
    from collections import Counter
    n = len(s)
    S = sorted(Counter(s).values())
    for x in range(int((10**n - 1)**0.5), int((10**(n - 1))**0.5) - 1, -1):
        y = x**2
        Y = sorted(Counter(str(y)).values())
        if S == Y:
            return y
    else:
        return -1
