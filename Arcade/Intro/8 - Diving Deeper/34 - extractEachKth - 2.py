def solution(inputArray, k):

    res = []
    while len(inputArray):
        res += inputArray[:k - 1]
        inputArray = inputArray[k:]
    
    return res