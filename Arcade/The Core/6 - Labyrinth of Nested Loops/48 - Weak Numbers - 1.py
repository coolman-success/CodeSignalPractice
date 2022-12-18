def solution(n):

    # Bruteforce to calculate the number of divisors
    d = [sum(x % d == 0 for d in range(1, x)) for x in range(1, n + 1)]
    w = [sum(x < y for y in d[:i]) for i, x in enumerate(d)]

    first = max(w)
    second = w.count(first)

    return [first, second]
