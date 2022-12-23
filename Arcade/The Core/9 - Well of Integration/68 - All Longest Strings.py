def solution(inputArray):

    maxlen = max(map(len, inputArray))
    return [word for word in inputArray if len(word) == maxlen]
