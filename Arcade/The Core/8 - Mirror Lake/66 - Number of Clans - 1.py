def solution(divisors, k):

    clans = set()
    for i in range(1, k + 1):
        divisor_vec = 0
        for j in range(len(divisors)):
            if i % divisors[j] == 0:
                divisor_vec |= 1 << j
        clans.add(divisor_vec)

    return len(clans)
