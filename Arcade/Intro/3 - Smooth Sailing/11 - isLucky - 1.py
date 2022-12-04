def solution(n):
    
    numstr = str(n)
    half = len(numstr)//2
    first_half = sum(int(d) for d in numstr[:half])
    second_half = sum(int(d) for d in numstr[half:])
    
    return first_half == second_half
