def solution(a):

    lsum = [sum(a[:i + 1]) for i in range(len(a))]
    split = lsum[-1]//3
    firstCut = [i for i in range(len(a)-2) if lsum[i] == split]

    return sum(lsum[i + 1:-1].count(2*split) for i in firstCut)
