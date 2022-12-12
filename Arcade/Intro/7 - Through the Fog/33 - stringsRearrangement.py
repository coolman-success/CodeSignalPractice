def solution(inputArray):

    from itertools import permutations
    for trial in permutations(inputArray):
        if all(sum(a != b for a, b in zip(x, y)) == 1 for x, y in zip(trial[:-1], trial[1:])):
            return True
    return False
