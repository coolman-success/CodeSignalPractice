def solution(s):
    from collections import Counter
    n = len(s)
    S = Counter(s).most_common()
    for x in range(int((10**n - 1)**0.5), int((10**(n - 1))**0.5) - 1, -1):
        y = x**2
        Y = Counter(str(y)).most_common()
        if len(S) == len(Y) and all(c[1] == d[1] for c, d in zip(S, Y)):
            return y
    else:
        return -1
