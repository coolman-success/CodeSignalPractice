def solution(a, b):

    return sorted(a) == sorted(b) and sum(x != y for x, y in zip(a, b)) < 3
