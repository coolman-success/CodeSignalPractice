def solution(n):
    import functools
    return [[0] * x for x in functools.reduce(lambda acc, i: acc + [acc[-1] + acc[-2]], range(n - 2), [0, 1])]
