def solution(morning, evening):
    return [[min(t) for t in zip(morning, evening)], [max(t) for t in zip(morning, evening)]]
