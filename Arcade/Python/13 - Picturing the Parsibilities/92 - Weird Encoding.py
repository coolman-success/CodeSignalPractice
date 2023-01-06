from base64 import b64decode

def solution(encoding, message):

    return b64decode(message, encoding).decode('utf-8')
