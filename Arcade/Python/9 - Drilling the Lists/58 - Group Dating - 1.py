def solution(male, female):
    return [
        [pair[0] for pair in zip(male, female) if pair[0] != pair[1]],
        [pair[1] for pair in zip(male, female) if pair[0] != pair[1]]
    ]
