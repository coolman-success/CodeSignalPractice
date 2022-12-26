def solution(a):

    return [(x + sum(a[i:]))%2 for i, x in enumerate(a)]
