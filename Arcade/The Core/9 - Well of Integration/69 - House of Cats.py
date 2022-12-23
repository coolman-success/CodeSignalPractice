def solution(legs):

    return list(range((legs % 4)//2, legs//2 + 1, 2))
