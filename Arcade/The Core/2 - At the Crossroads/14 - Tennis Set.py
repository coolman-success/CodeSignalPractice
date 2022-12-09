def solution(score1, score2):

    mins, maxs = min(score1, score2), max(score1, score2)
    return (maxs == 7 and mins in [5, 6]) or (maxs == 6 and mins < 5)
