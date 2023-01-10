def solution(items):

    res = []
    for i in range(len(items)):
        small = -1
        for x in items[:i][::-1]:
            if x < items[i]:
                small = x
                break
        res.append(small)
    return res
