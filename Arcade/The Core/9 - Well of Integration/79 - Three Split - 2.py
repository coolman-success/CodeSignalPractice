# !!! This solution doesn't meet the time constraint !!!
def solution(a):

    split = sum(a)//3
    left, right = [], []
    lsum, rsum, n = 0, 0, len(a)
    
    for i in range(n - 2):
        lsum += a[i]
        rsum += a[n - i - 1]
        if lsum == split:
            left.append(i + 1)
        if rsum == split:
            right.append(n - i - 1)
    
    return sum(i < j for i in left for j in right)
