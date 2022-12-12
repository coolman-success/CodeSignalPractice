def solution(n):

    # if n = a + (a + 1) + ... + (a + k), where k > 0
    #    n = (a + a + k)(k + 1)/2
    #   2n = (2a + k)(k + 1)
    # either (2a + k) or (k + 1) is odd and for each odd factor of 2n
    # it has a solution of making consecutive sums. the number of odd
    # factors by the way is the product of exponents added by 1.
    #   n = 3^e1 * 5^e2 * 7^e3 * ... 
    # the number of odd factors is calculated by the following expression
    #   (e1 + 1)(e2 + 1)(e3 + 1)...
    # the result should be subtracted by 1 because the number of factors also
    # counts 1 as a factor
    count = 1
    while n % 2 == 0:
        n /= 2
    odd = 3
    while odd <= n:
        exp = 0
        while n % odd == 0:
            n /= odd
            exp += 1
        count *= exp + 1
        odd += 2

    return count - 1
