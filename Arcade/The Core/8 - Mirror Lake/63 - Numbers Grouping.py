def solution(a):

    groups = [(x - 1)//10000 for x in a]
    return len(a) + len(set(groups))
