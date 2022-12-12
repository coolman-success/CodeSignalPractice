def solution(inputArray, k):

    del inputArray[k - 1::k]
    return inputArray