def solution(n):

    while n % 10 == 0:
        n = n // 10

    return '0' in str(n)
