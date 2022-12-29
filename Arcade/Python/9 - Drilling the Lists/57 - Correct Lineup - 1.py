def solution(athletes):
    return [athletes[i + (-1)**i] for i in range(len(athletes))]
