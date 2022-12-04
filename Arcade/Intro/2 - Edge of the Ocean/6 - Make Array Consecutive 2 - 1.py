def solution(statues):
    min_size, max_size = 21, 0
    for s in statues:
        if s > max_size: max_size = s
        if s < min_size: min_size = s
    
    return max_size - min_size + 1 - len(statues)
