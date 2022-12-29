from itertools import dropwhile, chain

def solution(pills):
    gen = chain(dropwhile(lambda x: len(x)%2, pills), [''] * 3)
    next(gen)
    return [next(gen) for _ in range(3)]
