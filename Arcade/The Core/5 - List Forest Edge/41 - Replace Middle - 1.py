def solution(arr):

    n = len(arr)
    if n & 1 == 0:
        arr[ n//2 - 1 : n//2 + 1 ] = [arr[n//2 - 1] + arr[n//2]]
    return arr
