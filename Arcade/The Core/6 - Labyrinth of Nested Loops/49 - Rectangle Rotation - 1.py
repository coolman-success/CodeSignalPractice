def solution(a, b):
    import math
    # inside the rectangle, if you count points in diagonal direction,
    # there are 2 types of point arrays with different lengths
    # the number of points locating 45 degree direction can be calculated
    # by multiplication of int(a/sqrt(2)) + 1 and int(b/sqrt(2)) + 1
    # the other points can be less than or greater than those by one.
    # it's determined by the decimal point number if it's greater than 0.5
    # or not.
    ahalf = (a/2**0.5)/2
    bhalf = (b/2**0.5)/2

    rect1 = [int(ahalf)*2 + 1, int(bhalf)*2 + 1]
    rect2 = [0, 0]

    rect2[0] = rect1[0] - 1 if ahalf - int(ahalf) < 0.5 else rect1[0] + 1
    rect2[1] = rect1[1] - 1 if bhalf - int(bhalf) < 0.5 else rect1[1] + 1

    count = rect1[0]*rect1[1] + rect2[0]*rect2[1]

    return count
