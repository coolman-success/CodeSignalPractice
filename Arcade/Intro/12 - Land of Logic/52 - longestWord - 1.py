def solution(text):
    import re
    return max(re.findall(r'\w+', text), key=len)
