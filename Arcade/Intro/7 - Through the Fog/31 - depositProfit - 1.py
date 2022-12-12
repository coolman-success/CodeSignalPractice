def solution(deposit, rate, threshold):
    import math
    return math.ceil( math.log(threshold/deposit) / math.log((100 + rate)/100) )
