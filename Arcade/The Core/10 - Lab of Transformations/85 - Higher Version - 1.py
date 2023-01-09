def solution(ver1, ver2):

    for v1, v2 in zip(ver1.split("."), ver2.split(".")):
        if int(v1) > int(v2):
            return True
        if int(v1) < int(v2):
            return False
    return False
