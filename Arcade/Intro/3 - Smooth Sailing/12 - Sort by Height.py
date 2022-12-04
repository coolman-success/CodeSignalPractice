def solution(a):
    
    people = sorted([h for h in a if h != -1])
    
    return [people.pop(0) if h != -1 else -1 for h in a]
