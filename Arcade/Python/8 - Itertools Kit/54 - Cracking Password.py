from itertools import product, filterfalse

def solution(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return sorted(x for x in map(createNumber, product(digits, repeat=k)) if not int(x)%d)
