def solution(inputString):

    return ''.join([chr(ord("z") - ord(c) + ord("a")) for c in inputString])
