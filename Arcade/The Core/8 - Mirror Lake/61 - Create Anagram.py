def solution(s, t):

    return sum(max(0, s.count(ch) - t.count(ch)) for ch in set(s))
