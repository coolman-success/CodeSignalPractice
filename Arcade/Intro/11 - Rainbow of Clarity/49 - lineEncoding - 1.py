def solution(s):
    import re
    return re.sub(r'(.)\1+', lambda x: str(len(x.group())) + x.group(1), s)
