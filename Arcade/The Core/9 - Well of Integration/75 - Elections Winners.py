def solution(votes, k):

    m = max(votes)
    if k == 0:
        return 1 if votes.count(m) == 1 else 0
    return len([v for v in votes if v + k > m])
