def solution(n):

    nonzero = False
    for d in str(n)[::-1]:
        if nonzero and d == '0':
            return True
        elif d != '0':
            nonzero = True

    return False
