def solution(comb1, comb2):

    res = len(comb1) + len(comb2)
    for offset in range(-len(comb2) + 1, len(comb1) - 1):
        low1, low2 = max(offset, 0), min(offset, 0)
        high1, high2 = min(len(comb1), offset + len(comb2)), max(len(comb1), offset + len(comb2))
        overlap = True
        for i in range(low1, high1):
            j = (i - low1)*(low2 == 0) + (low1 - low2 + i)*(low2 < 0)
            if comb1[i] == "*" and comb2[j] == "*":
                overlap = False
                break
        if overlap and high2 - low2 < res:
            res = high2 - low2
    return res
