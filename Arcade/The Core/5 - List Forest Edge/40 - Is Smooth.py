def solution(arr):

    n = len(arr)
    return arr[0] == sum(arr[(n -1)//2:n//2 + 1]) == arr[-1]
