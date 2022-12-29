def solution(participants):
    return [p[0] for p in enumerate(participants) if p[0] > p[1]]
