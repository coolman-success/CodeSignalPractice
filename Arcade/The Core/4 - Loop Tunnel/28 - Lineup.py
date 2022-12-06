def solution(commands):

    count = 0
    same = True
    for command in commands:
        if command in ["L", "R"]:
            same = not same
        if same:
            count += 1
    
    return count
