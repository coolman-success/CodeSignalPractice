def solution(text):
    import re
    return max(re.findall(r'[a-zA-Z]+', text), key=len)
