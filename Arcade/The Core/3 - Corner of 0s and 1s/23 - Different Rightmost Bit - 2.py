def solution(n, m):
    return [1 << i for i, b in enumerate(bin(n ^ m)[::-1]) if b == '1'][0]
