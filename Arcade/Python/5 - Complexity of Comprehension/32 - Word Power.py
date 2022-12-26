def solution(word):
    import string
    num = dict(zip(string.ascii_lowercase, range(1, 27)))
    return sum([num[ch] for ch in word])
