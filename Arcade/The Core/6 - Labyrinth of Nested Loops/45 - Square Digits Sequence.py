def solution(a0):

    a = []
    while a0 not in a:
        a.append(a0)
        a0 = sum(int(d)**2 for d in str(a0))
    
    return len(a) + 1
