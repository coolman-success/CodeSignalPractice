def solution(a, b):
    return sum([x for x in range(max(a, 2), b + 1) if all([x%y for y in range(2, int(x**0.5 + 1))])])
