from itertools import product, filterfalse

def solution(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return sorted(map(createNumber, filterfalse(lambda x: int(createNumber(x))%d, product(digits, repeat=k))))
