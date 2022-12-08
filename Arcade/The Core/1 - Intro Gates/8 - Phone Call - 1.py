def solution(min1, min2_10, min11, s):

    def get_cost(t):
        return min1 if t < 1 else min2_10 if t < 10 else min11
        
    res = 0
    while s >= get_cost(res):
        s -= get_cost(res)
        res += 1
    return res
