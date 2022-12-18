def solution(code):

    asciis = [int(code[i:i + 8], 2) for i in range(0, len(code), 8)]
    return ''.join(c for c in map(chr, asciis))
