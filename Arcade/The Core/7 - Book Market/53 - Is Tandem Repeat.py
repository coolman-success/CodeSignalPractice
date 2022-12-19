def solution(inputString):

    n = len(inputString)
    return inputString[:n//2] == inputString[n//2:]
