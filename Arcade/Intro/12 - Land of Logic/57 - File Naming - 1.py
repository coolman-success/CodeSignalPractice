def solution(names):

    res = []
    for name in names:
        if name in res:
            cnt = 1
            while name + f'({cnt})' in res:
                cnt += 1
            res.append(name + f'({cnt})')
        else:
            res.append(name)
    
    return res
