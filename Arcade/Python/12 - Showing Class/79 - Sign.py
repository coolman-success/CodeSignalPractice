class Functions(object):
    @staticmethod
    def solution(x):
        return (x > 0) - (x < 0)

def solution(x):
    return Functions.solution(x)
