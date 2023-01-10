def solution(inputArray):

    step = 1
    while len(inputArray) != 1:
        inputArray = [
            inputArray[i] + inputArray[i + 1] if step % 2
            else inputArray[i] * inputArray[i + 1]
            for i in range(0, len(inputArray), 2)
        ]
        step += 1
    
    return inputArray[0]
