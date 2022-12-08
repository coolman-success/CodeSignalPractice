def solution(n):

    quotient, remainder = divmod(n, 60)
    return sum(int(d) for d in str(quotient*100 + remainder))
