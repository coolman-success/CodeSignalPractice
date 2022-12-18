def solution(n):

    x = str(n)
    return max(int(x[:i] + x[i + 1:]) for i in range(len(x)))
