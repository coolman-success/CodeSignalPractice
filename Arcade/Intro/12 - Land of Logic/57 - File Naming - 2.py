def solution(names):

    for name in names:
        cnt = 1
        for i in [i for i, comp in enumerate(names) if comp == name][1:]:
            while name + f'({cnt})' in names[:i]:
                cnt += 1
            names[i] += f'({cnt})'
    
    return names
