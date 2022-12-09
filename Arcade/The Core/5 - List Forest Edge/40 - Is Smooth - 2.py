def solution(arr):

    n = len(arr)
    middle = arr[n//2] if n % 2 else arr[n//2] + arr[n//2 - 1]
    return arr[0] == middle == arr[-1]
