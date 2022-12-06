def solution(n):
    return sum([(b=='1') << (i-1) if i%2 else (b=='1') << (i+1) for i, b in enumerate(bin(n)[:1:-1])])
