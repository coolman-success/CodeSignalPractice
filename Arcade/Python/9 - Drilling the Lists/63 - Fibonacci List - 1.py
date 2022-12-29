def solution(n):
    import functools
    return [[0] * x for x in functools.reduce(lambda acc, i: acc + [acc[i - 1] + acc[i - 2]], range(2, n), [0, 1])]
