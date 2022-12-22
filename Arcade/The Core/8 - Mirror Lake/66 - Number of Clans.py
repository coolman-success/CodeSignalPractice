def solution(divisors, k):

    clans = set(tuple(x % y == 0 for y in divisors) for x in range(1, k + 1))

    return len(clans)
