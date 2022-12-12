def solution(inputString):

    res = ''
    for ch in inputString:
        res += chr((ord(ch) - ord('a') + 1) % 26 + ord('a'))
    return res
