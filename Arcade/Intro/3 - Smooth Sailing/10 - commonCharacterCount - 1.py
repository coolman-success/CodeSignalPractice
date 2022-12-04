def solution(s1, s2):
    
    from collections import Counter
    
    freq1 = Counter(s1)
    freq2 = Counter(s2)
    common = freq1 & freq2
    
    return common.total()
