def solution(numbers):
    import functools
    return functools.reduce(lambda acc, i: acc + numbers[i] if i % 2 else acc * numbers[i], range(1, len(numbers)), numbers[0])
