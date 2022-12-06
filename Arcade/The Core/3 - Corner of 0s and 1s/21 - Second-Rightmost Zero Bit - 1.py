def solution(n):
    return [2**i for i, b in enumerate(bin(n)[::-1]) if b == '0'][1]
