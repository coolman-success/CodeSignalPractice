def solution(male, female):
    return [[], []] if male==female else list(zip(*[x for x in zip(male,female) if x[0]!=x[1]]))
