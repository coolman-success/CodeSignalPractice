def solution(s):

    return all(c1 < c2 for c1, c2 in zip(s, s[1:]))
