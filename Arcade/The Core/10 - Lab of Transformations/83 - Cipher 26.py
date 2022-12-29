def solution(message):

    acc = 0
    decrypted = ""
    for c in message:
        ch = ord(c) - ord('a') + 26
        cur = (ch - acc) % 26
        decrypted += chr(cur + ord('a'))
        acc = ch
    return decrypted
