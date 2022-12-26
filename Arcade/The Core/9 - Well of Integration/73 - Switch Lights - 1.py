def solution(a):

    for i in range(len(a)):
        if not a[i]:
            continue
        for j in range(i + 1):
            a[j] = 1 - a[j]
    return a
