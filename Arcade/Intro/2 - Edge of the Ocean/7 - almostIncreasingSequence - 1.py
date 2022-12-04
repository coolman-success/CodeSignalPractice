def solution(sequence):
    violate = index = 0
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            violate += 1
            index = i
            if violate > 1:
                return False
    
    if index == 0 or index == len(sequence) - 2:
        return True

    if sequence[index - 1] < sequence[index + 1]:
        return True
        
    if sequence[index] < sequence[index + 2] and index < len(sequence) - 2:
        return True
    
    return False
