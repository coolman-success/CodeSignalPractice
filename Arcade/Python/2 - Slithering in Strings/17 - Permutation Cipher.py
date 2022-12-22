def solution(password, key):
    import string
    table = str.maketrans(string.ascii_lowercase, key)
    return password.translate(table)
