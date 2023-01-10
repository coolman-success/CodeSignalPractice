def solution(shoes):

    lefts, rights = [], []
    
    for side in shoes:
        if side[0] == 0:
            lefts.append(side[1])
        else:
            rights.append(side[1])
    
    return sorted(lefts) == sorted(rights)
