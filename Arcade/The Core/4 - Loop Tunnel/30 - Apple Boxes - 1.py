def solution(k):

    return sum((-1)**(x + 1) * (x + 1)**2 for x in range(k))
