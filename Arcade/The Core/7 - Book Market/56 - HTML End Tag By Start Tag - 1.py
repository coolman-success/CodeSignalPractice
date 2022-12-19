def solution(startTag):
    import re
    return "</" + re.search('\w+', startTag).group() +">"
