def solution(cipher):

    temp = 0
    res = []
    for c in cipher:
        temp = temp*10 + int(c)
        if temp >= ord('a'):
            res.append(chr(temp))
            temp = 0
    
    return ''.join(res)
