def solution(inputArray, result):

    from itertools import combinations
    
    count = 0
    for a, b in combinations(inputArray, 2):
        count += all(c in [a[i], b[i]] for i, c in enumerate(result))
    
    return count
