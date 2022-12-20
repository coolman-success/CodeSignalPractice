def solution(s, t):

    from collections import Counter
    return len(list((Counter(t) - Counter(s)).elements()))
