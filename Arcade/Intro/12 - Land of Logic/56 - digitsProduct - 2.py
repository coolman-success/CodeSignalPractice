def solution(product):

    if product == 0:
        return 10
    elif product < 10:
        return product
    
    small_pos = 0
    while product > 9:
        orig = product
        for f in range(9, 1, -1):
            if product % f == 0:
                next_num = solution(product//f)
                if next_num == -1:
                    continue
                small_pos = next_num*10 + f
                product = f
                break
        if product == orig:
            return -1
    
    return small_pos
