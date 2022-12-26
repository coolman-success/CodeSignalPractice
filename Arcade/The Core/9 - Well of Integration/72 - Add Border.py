def solution(picture):

    n = len(picture[0])
    return ["*"*(n + 2)] + ["*" + word + "*" for word in picture] + ["*"*(n + 2)]
