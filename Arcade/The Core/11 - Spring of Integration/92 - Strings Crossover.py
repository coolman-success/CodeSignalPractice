def solution(inputArray, result):

    from itertools import combinations
    
    return sum(
        all(x in p for x, p in zip(result, zip(a, b)))
        for a, b in combinations(inputArray, 2))
