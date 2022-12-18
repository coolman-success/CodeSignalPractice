def solution(current, numberOfDigits):

    while numberOfDigits >= len(str(current)):
        numberOfDigits -= len(str(current))
        current += 1
    
    return current - 1
