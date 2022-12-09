def solution(inputArray):
    
    s = sorted(inputArray)
    for jump in range(2, s[-1] + 2):
        if all(jump*i not in s for i in range(s[-1]//jump + 2)):
            return jump
