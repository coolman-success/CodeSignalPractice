def solution(inputArray):

    while len(inputArray)>=4:
        inputArray = [
            (inputArray[i] + inputArray[i + 1])*(inputArray[i + 2] + inputArray[i + 3])
            for i in range(0, len(inputArray), 4)
        ]
    
    return inputArray[0] if len(inputArray) == 1 else inputArray[0] + inputArray[1]
