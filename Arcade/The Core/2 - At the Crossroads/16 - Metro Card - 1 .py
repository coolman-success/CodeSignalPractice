def solution(lastNumberOfDays):

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    return list(set(n for d, n in zip(days, days[1:] + days[:1]) if d == lastNumberOfDays))
