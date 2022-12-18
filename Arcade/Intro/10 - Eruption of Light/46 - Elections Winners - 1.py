def solution(votes, k):

    max_vote = max(votes)
    if k == 0:
        return 1 if votes.count(max_vote) == 1 else 0
    return len([v for v in votes if max_vote < v + k])
