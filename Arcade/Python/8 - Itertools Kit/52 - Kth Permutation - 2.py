from itertools import permutations, dropwhile, count

def solution(numbers, k):
    return next(dropwhile(lambda x: x[1] < k - 1, zip(permutations(numbers), count())))[0]
