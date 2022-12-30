def solution(number):
    def fractions():
        level = [[1, 1]]
        yield [1, 1]
        
        while True:
            temp = []
            for r in level:
                a, b = r[0], r[1]
                temp.append([a, a + b])
                yield [a, a + b]
                temp.append([a + b, b])
                yield [a + b, b]
            level = temp

    gen = fractions()
    res = 0
    while next(gen) != number:
        res += 1
    return res
