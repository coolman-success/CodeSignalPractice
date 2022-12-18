def solution(product):

    if product == 0:
        return 10

    for test in range(10000):
        prod = 1
        for d in str(test):
            prod *= int(d)
        if prod == product:
            return test
    
    return -1
