def solution(a):

    split = sum(a)//3
    acc = count = first = 0
    
    for i in range(len(a) - 1):
        acc += a[i]
        if acc == split:
            first += 1
        if acc == split*2:
            count += first - (split == 0)
    
    return count
