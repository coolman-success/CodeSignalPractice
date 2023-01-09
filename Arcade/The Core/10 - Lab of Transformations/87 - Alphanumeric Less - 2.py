def solution(s1, s2):
    import re
    seq1 = re.findall(r'\D|\d+', s1)
    seq2 = re.findall(r'\D|\d+', s2)

    if s1 == s2:
        return False

    for t1, t2 in zip(seq1, seq2):
        if t1 == t2:
            continue
        if len(t1) == 1 or len(t2) == 1:
            return t1 < t2
        elif int(t1) != int(t2):
            return int(t1) < int(t2)

    if len(seq1) != len(seq2):
        return len(seq1) < len(seq2)

    for t1, t2 in zip(seq1, seq2):
        if 'a' <= t1 <= 'z':
            pass
        if len(t1) != len(t2):
            return len(t1) > len(t2)
