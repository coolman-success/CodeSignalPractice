def solution(inputArray, k):

    return max(sum(inputArray[i:i + k]) for i in range(len(inputArray) - k + 1))