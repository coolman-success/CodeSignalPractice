def solution(upSpeed, downSpeed, desiredHeight):
    import math
    return math.ceil((desiredHeight - upSpeed)/(upSpeed - downSpeed) + 1) if desiredHeight > upSpeed else 1