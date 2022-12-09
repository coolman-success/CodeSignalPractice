def solution(inputArray):
    
    jump = 2
    while True:
        if all(x % jump for x in inputArray):
            return jump
        jump += 1
