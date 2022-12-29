def solution(line):

    line = line.replace("_", "")
    if line.count("#") == 0:
        base, number = 10, line
    elif line.count("#") == 2 and line[-1] == "#":
        base, number = line[:-1].split("#")
    else:
        return False
    
    try:
        if int(base) > 16 or int(base) < 2:
            return False
        int(number, int(base))
        return True
    except ValueError:
        return False
