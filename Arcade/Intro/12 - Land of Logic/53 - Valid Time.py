def solution(time):
    import re
    if not re.match(r'^\d\d:\d\d$', time):
        return False
    return 0 <= int(time[:2]) < 24 and 0 <= int(time[3:]) < 60
