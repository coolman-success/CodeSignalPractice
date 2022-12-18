def solution(address):
    import re
    return re.search(r'@[a-zA-Z0-9-.]+$', address).group()[1:]