def solution(a, b):

    diff = [[x, y] for x, y in zip(a, b) if x != y]
    return len(diff) == 0 or (len(diff) == 2 and diff[0] == diff[1][::-1])
