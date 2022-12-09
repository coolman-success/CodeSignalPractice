def solution(a, b, c):

    return any([a + b == c,
                a - b == c,
                a * b == c,
                a / b == c])
