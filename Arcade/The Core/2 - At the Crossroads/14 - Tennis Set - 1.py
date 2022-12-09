def solution(score1, score2):

    if max(score1, score2) > 7:
        return False
    elif 6 in [score1, score2] and abs(score1 - score2) > 1:
        return True
    elif 7 in [score1, score2] and abs(score1 - score2) in [1, 2]:
        return True
    else:
        return False
