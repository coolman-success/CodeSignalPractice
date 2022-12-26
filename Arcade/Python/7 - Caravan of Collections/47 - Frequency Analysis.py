from collections import Counter

def solution(encryptedText):
    return Counter(encryptedText).most_common()[0][0]
