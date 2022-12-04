def solution(s1, s2):
    
    return sum(min(s1.count(ch), s2.count(ch)) for ch in set(s1))
