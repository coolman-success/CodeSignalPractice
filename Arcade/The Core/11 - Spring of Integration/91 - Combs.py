def solution(comb1, comb2):

    b1 = ''.join(['0' if x == '.' else '1' for x in comb1])
    b2 = ''.join(['0' if x == '.' else '1' for x in comb2])
    b1, b2 = int(b1, 2), int(b2, 2)

    l1, l2 = len(comb1), len(comb2)
    res = l1 + l2

    for i in range(l1):
        if (b2 << i) & b1 == 0:
            tmp = max(l2 + i, l1)
            res = min(res, tmp)
    
    for i in range(l2):
        if (b1 << i) & b2 == 0:
            tmp = max(l1 + i, l2)
            res = min(res, tmp)
    
    return res
