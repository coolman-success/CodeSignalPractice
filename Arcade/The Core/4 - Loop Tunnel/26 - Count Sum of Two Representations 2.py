def solution(n, l, r):

    return sum(l <= A <= n - A <= r for A in range(l, r + 1))
