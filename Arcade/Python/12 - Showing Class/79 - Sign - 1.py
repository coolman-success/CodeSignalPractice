class Functions(object):
    def solution(x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0

def solution(x):
    return Functions.solution(x)
