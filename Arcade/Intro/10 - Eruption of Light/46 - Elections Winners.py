def solution(votes, k):

    max_vote = max(votes)
    
    return int(votes.count(max_vote) == 1) if k == 0 else len([v for v in votes if max_vote < v + k])
