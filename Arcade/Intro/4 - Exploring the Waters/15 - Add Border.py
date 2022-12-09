def solution(picture):
    
    cols = len(picture[0])
    res = ['*'*(cols + 2)]
    
    for line in picture:
        res.append('*' + line + '*')
    
    res.append(res[0])
    
    return res
