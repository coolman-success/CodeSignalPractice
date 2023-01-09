def solution(s1, s2):
    import re
    seq1 = re.findall(r'\D|\d+', s1)
    seq2 = re.findall(r'\D|\d+', s2)
    
    s1 = [(0, int(t), -t.count('0')) if t.isdigit() else (1, t) for t in seq1]
    s11 = [token[:2] for token in s1]
    s2 = [(0, int(t), -t.count('0')) if t.isdigit() else (1, t) for t in seq2]
    s21 = [token[:2] for token in s2]
    
    return (s11 < s21) or ((s11 == s21) and (s1 < s2))
