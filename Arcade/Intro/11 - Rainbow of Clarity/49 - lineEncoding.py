def solution(s):

    from itertools import groupby
    res = ''
    for key, group in groupby(s):
        length = len(list(group))
        res += str(length) + key if length > 1 else key
    
    return res
