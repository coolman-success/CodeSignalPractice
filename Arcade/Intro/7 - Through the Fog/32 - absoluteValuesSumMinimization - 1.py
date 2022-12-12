def solution(a):

    min_sum = sum([abs(x - a[0]) for x in a])
    min_ele = a[0]
    for c in a[1:]:
        temp = sum([abs(x - c) for x in a])
        if min_sum > temp:
            min_sum, min_ele = temp, c
    
    return min_ele