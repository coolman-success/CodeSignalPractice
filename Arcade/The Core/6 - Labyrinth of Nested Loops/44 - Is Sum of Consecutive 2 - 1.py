def solution(n):

    # Bruteforce method
    count = 0
    for i in range(1, n//2 + 1):
        temp = 0
        j = i
        while temp < n:
            temp += j
            j += 1
        if temp == n:
            count += 1

    return count
