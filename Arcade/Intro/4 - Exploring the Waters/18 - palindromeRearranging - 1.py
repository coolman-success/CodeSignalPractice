def solution(inputString):
    
    from collections import Counter
    freq = Counter(inputString)
    return sum(freq[key]%2 != 0 for key in freq) < 2
