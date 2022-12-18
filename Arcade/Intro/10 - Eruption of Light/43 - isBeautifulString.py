def solution(inputString):

    freq = [0] * 26
    for c in inputString:
        freq[ord(c) - ord('a')] += 1
    return all(x >= y for x, y in zip(freq, freq[1:]))
