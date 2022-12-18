def solution(n):

    # get number of divisors based on factorization
    def divisors(x):
        if x == 1:
            return 1
        d, res = 2, 1
        while x != 1:
            e = 0
            while x % d == 0:
                e += 1
                x /= d
            res *= e + 1
            d += 1
        return res
    
    d = [divisors(x) for x in range(1, n + 1)]
    weakness = [sum(d[i] < d[j] for j in range(1, i)) for i in range(n)]

    first = max(weakness)
    second = weakness.count(first)

    return [first, second]
