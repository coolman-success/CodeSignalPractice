def solution(sequence):
    false1 = false2 = 0
    
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            false1 += 1
            if false1 > 1:
                return False
    
    for i in range(len(sequence) - 2):
        if sequence[i] >= sequence[i + 2]:
            false2 += 1
            if false2 > 1:
                return False
    
    return True
