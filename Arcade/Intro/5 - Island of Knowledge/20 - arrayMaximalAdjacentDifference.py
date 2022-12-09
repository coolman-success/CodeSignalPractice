def solution(inputArray):
    return max(abs(x - y) for x, y in zip(inputArray[1:], inputArray[:-1]))
