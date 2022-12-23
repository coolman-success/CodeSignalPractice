def solution(students):
    return sum((-1)**i*number for (i, number) in enumerate(students))
