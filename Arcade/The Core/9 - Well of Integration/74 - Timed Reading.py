def solution(maxLength, text):
    import re
    text = re.sub(r'[^a-zA-Z\s]', "", text)
    return len(list(word for word in text.split() if len(word) <= maxLength))
