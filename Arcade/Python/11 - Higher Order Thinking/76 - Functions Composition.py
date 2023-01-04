def compose(functions):
    import functools
    return lambda x: functools.reduce(lambda f, g: g(f), reversed(list(functions)), x)

def solution(functions, x):
    return compose(map(eval, functions))(x)
