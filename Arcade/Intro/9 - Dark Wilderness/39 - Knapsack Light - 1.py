def solution(value1, weight1, value2, weight2, maxW):

    def getValue(value, weight):
        return value if weight <= maxW else 0
    
    if weight1 + weight2 <= maxW:
        return value1 + value2
    else:
        return max(getValue(value1, weight1), getValue(value2, weight2))