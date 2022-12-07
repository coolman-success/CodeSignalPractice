def solution(k):

    return sum((x + 1)**2 if x%2 else -(x + 1)**2 for x in range(k))
