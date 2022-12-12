def solution(deposit, rate, threshold):
    import math
    return math.ceil( math.log(threshold/deposit, (100 + rate)/100) )
