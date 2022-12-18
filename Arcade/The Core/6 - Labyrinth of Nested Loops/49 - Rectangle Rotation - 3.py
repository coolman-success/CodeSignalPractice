def solution(a, b):
    import math
    # all x, y <= ((a/2)**2 + (b/2)**2)**0.5
    # plane rotation matrix
    #   ┌    ┐   ┌               ┐┌   ┐
    #   │ d1 │ - │ cos θ  -sin θ ││ x │
    #   │ d2 │ - │ sin θ   cos θ ││ y │
    #   └    ┘   └               ┘└   ┘
    r = int(((a/2)**2 + (b/2)**2)**0.5)
    sine = math.sin(math.radians(45))
    cosine = math.cos(math.radians(45))
    
    count = 0
    for x in range(-r, r + 1):
        for y in range(-r, r + 1):
            d1 = x*cosine - y*sine
            d2 = x*sine + y*cosine

            # check if it's inside the box
            if -a/2 <= d1 <= a/2 and -b/2 <= d2 <= b/2:
                count += 1

    return count
