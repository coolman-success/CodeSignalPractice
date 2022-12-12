def solution(s):

    from collections import Counter
    c = Counter(s)
    return len(c.keys())