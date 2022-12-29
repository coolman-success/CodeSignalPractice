def solution(number):

    a = ord('A')
    number = ord(number) - a
    return [chr(x + a) + ' + ' + chr(number - x + a) for x in range(number//2 + 1)]
