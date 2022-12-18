def solution(product):

    if product == 0:
        return 10
    elif product == 1:
        return 1
    
    res = []
    while product > 1:
        for f in range(9, 1, -1):
            if product % f == 0:
                res.append(f)
                product //= f
                break
        else:
            return -1
    
    return int("".join(map(str, sorted(res))))
