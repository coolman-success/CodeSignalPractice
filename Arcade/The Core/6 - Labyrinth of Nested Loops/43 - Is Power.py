def solution(n):

    if n == 1:
        return True
    for a in range(2, int(n**0.5) + 1):
        test = n
        while test % a == 0:
            test //= a
        if test == 1:
            return True
    return False
