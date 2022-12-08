def solution(candlesNumber, makeNew):

    answer = leftover = 0
    while candlesNumber:
        answer += candlesNumber
        leftover += candlesNumber
        candlesNumber = leftover // makeNew
        leftover = leftover % makeNew
    
    return answer
