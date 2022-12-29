def solution(line):

    line = line.replace('_', '')

    if line.isdigit(): 
        return True
    try:
        base, number = line.split('#')[:-1]
        if int(base) < 2 or int(base) > 16:
            return False
        try:
            int(number, int(base))
            return True
        except ValueError:
            return False
    except ValueError:
        return False
