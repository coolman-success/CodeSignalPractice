def solution(a, b):
    import math
    # surrounding lines: y = x + a/sqrt(2)
    #                    y = x - a/sqrt(2)
    #                    y = -x + b/sqrt(2)
    #                    y = -x - b/sqrt(2)
    # coordinates of corners: ±(a - b)/(2⋅sqrt(2))
    #                         ±(a + b)/(2⋅sqrt(2))
    r2 = 2**0.5
    x1, x2 = (a - b)/2/r2, (a + b)/2/r2
    v = sorted([x1, x2, -x1, -x2])
    
    count = 0
    for x in range(int(v[0]), int(v[3]) + 1):
        if v[0] <= x < v[1]:
            y1, y2 = x + a/r2, -x - b/r2
        elif v[1] <= x < v[2]:
            if a >= b:
                y1, y2 = x + b/r2, x - b/r2
            else:
                y1, y2 = -x + a/r2, -x - a/r2
        elif v[2] <= x < v[3]:
            y1, y2 = -x + a/r2, x - b/r2
        
        # count the number of integers in [y1, y2]
        count += math.floor(y1) - math.ceil(y2) + 1
    
    return count
