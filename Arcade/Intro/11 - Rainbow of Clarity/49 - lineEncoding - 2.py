def solution(s):

    res = ch = ''
    cnt = 1
    for c in s + '0':
        if ch == c:
            cnt += 1
        else:
            res += ch if cnt == 1 else str(cnt) + ch
            cnt = 1
            ch = c
    
    return res
