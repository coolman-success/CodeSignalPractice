from collections import Counter

def solution(shoes):

    lefts = [x[1] for x in shoes if x[0] == 0]
    rights = [x[1] for x in shoes if x[0] == 1]
    
    l = Counter(lefts)
    r = Counter(rights)
    
    return l == r
