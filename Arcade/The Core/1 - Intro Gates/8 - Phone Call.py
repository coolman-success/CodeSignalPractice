def solution(min1, min2_10, min11, s):

    if s < min1:
        return 0
    elif s < min1 + min2_10*9:
        return (s - min1)//min2_10 + 1
    else:
        return (s - min1 - min2_10*9)//min11 + 10
