def solution(cipher):

    cipher = cipher.replace('97', '097').replace('98', '098').replace('99', '099')
    res = [chr(int(cipher[i:i + 3])) for i in range(0, len(cipher), 3)]

    return ''.join(res)
