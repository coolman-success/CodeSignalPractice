import re

def solution(cipher):

    codes = re.findall(r'1?\d\d', cipher)

    return "".join(chr(int(code)) for code in codes)
