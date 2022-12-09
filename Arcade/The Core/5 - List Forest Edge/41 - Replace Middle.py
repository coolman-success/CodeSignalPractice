def solution(arr):

    n = len(arr)
    return arr[:(n - 1)//2] + [sum(arr[(n - 1)//2:n//2 + 1])] + arr[n//2 + 1:]
