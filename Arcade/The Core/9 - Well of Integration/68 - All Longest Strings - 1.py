def solution(inputArray):

    maxlen = len(max(inputArray, key=len))
    return [word for word in inputArray if len(word) == maxlen]
