def solution(a, b):

    return min(b.count(ch)//a.count(ch) for ch in set(a))
