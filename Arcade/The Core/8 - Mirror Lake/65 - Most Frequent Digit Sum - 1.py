def solution(n):

    def s(x):
        res = 0
        while x:
            res += x % 10
            x //= 10
        return res
    
    ss = []
    while n:
        ss.append(s(n))
        n = n - s(n)
    ss = sorted(ss, reverse=True)
    return max(ss, key=ss.count)
