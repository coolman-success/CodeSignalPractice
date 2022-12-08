def solution(arr):

    if arr:
        arr[0], arr[-1] = arr[-1], arr[0]
    return arr
