def solution(password, key):
    table = password.maketrans("abcdefghijklmnopqrstuvwxyz", key)
    return password.translate(table)
