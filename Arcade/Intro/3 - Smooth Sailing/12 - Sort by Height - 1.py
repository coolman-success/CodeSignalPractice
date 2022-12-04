def solution(a):
    
    people = [h for h in a if h != -1]
    people.sort()
    
    res = []
    for h in a:
        res += [-1] if h == -1 else [people.pop(0)]
    
    return res
