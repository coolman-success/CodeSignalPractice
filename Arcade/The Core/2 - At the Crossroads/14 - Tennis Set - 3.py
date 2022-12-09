def solution(score1, score2):

    if {score1, score2} == {5, 6}:
        return False
    elif {score1, score2} == {7, 5}:
        return True
    elif 6 in [score1, score2]:
        return True
    else:
        return False
