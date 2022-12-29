def solution(message):

    from string import ascii_lowercase as a

    s, n = "", 0
    for c in message:
        s += a[(a.find(c) - n)%26]
        n += (a.find(c) - n)%26

    return s
