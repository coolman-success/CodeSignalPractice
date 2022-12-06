def solution(n, l, r):

    if l > n/2 or r < n/2:
        return 0
    A, B = n//2, (n + 1)//2
    return min(A - l + 1, r - B + 1)
