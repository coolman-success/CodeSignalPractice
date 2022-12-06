def solution(commands):

    parity = count = 0
    for command in commands:
        parity += 1 if command == "L" else -1 if command == "R" else 0
        if parity % 2 == 0:
            count += 1
    
    return count
