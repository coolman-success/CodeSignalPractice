def solution(names):

    for i in range(len(names)):
        if names[i] in names[:i]:
            cnt = 1
            while names[i] + f'({cnt})' in names[:i]:
                cnt += 1
            names[i] += f'({cnt})'
    
    return names
