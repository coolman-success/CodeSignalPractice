def solution(st):

    i, n = 0, len(st)
    while st != st[::-1]:
        st = st[:n] + st[i] + st[n:]
        i += 1
    
    return st
