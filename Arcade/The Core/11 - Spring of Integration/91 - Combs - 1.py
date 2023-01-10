def solution(comb1, comb2):
    from itertools import zip_longest
    b1 = ''.join(['0' if x == '.' else '1' for x in comb1])
    b2 = ''.join(['0' if x == '.' else '1' for x in comb2])
    b1 = '0' * len(b2) + b1
    r = []
    for i in range(len(b1)):
        x = b1[:i]
        for a, b in zip_longest(b1[i:], b2, fillvalue='0'):
            x += str(int(a) + int(b))
        if not '2' in x:
            r.append(x.strip('0'))
    return len(sorted(r, key=len)[0])
