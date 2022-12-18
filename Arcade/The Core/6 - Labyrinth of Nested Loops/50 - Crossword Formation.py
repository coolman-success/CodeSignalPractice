def solution(words):

    def checkcrosswords(crosswords):
        formation = 0
        hword1, vword1, vword2, hword2 = crosswords
        
        for i in range(len(hword1) - 2):
            for k in range(len(vword1) - 2):
                if hword1[i] != vword1[k]:
                    continue
                for j in range(i + 2, len(hword1)):
                    for l in range(len(vword2) - 2):
                        if hword1[j] != vword2[l]:
                            continue
                        hoffset, voffset = j - i, l - k
                        for p in range(0, len(hword2) - hoffset):
                            for q in range(k + 2, len(vword1)):
                                if q + voffset < len(vword2) and \
                                    hword2[p] == vword1[q] and \
                                    hword2[p + hoffset] == vword2[q + voffset]:
                                    formation += 1
        return formation
    
    from itertools import permutations
    
    count = 0
    for crosswords in permutations(words):
        count += checkcrosswords(crosswords)
    
    return count
