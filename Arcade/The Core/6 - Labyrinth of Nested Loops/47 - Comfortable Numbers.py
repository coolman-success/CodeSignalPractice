def solution(l, r):

    count = 0
    for a in range(l, r + 1):
        sa = sum(int(d) for d in str(a))
        for b in range(a + 1, r + 1):
            sb = sum(int(d) for d in str(b))
            if a - sa <= b <= a + sa and b - sb <= a <= b + sb:
                count += 1
            if b > sa + a:
                break
    
    return count
