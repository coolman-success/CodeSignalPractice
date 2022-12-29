def solution(morning, evening):
    return [list(map(op, zip(morning, evening))) for op in [min, max]]
