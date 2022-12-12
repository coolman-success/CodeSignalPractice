def solution(inputArray, k):

    temp = max_sum = sum(inputArray[:k])
    for i in range(len(inputArray) - k):
        temp += inputArray[i + k] - inputArray[i]
        if temp > max_sum:
            max_sum = temp
    
    return max_sum