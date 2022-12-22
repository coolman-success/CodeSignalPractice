def solution(code):
    import re
    return re.sub(r'\s+', ' ', code).strip()
