def solution(a, b):
    return sum([x for x in range(a, b + 1) if not any([y for y in range(2, int(x**0.5 + 1)) if x%y==0]) and x!=1])
