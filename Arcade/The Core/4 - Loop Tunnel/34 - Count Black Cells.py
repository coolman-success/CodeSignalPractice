def solution(n, m):

    # As example 1 shows, the diagonal line crosses all vertical and horizontal
    # grid lines inside the box, so that the number of black cells is the sum of
    # the numbers of those lines (plus one) --- (n - 1) + (m - 1) + 1
    # Whenever the diagonal line passes the corner of squares inside the box as
    # shown in example 2, the number of black cells increases by the number of
    # cross points inside the box --- (m + n - 1) + (gcd(m, n) - 1)
    import math
    return (m + n - 1) + math.gcd(m, n) - 1
