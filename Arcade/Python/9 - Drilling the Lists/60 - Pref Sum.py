def solution(a):
    return [sum(a[:i + 1]) for i in range(len(a))]
