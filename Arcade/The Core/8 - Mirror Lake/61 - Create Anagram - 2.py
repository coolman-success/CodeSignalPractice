def solution(s, t):

    for ch in s:
        t = t.replace(ch, "", 1)
    return len(t)
