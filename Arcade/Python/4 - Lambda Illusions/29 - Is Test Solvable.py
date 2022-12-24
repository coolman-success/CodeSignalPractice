def solution(ids, k):
    digitSum = lambda id: sum(map(int, str(id)))

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0
