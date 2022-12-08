def solution(n):

    hh = str(n // 60)
    mm = str(n % 60)
    return sum(int(d) for d in hh + mm)
