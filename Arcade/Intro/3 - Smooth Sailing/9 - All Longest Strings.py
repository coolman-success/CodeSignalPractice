def solution(inputArray):
    
    longest = len(max(inputArray, key=len))
    
    return [word for word in inputArray if len(word) == longest]
