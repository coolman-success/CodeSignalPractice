def solution(a, b):

    from collections import Counter
    x, y = Counter(a), Counter(b)
    return min(y[k]//x[k] for k in x)
