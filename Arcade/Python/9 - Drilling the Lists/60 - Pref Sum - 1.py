def solution(a):
    import functools
    return functools.reduce(lambda acc, x: acc + [acc[-1] + x], a, [0])[1:]
