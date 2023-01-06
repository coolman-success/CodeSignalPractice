from html.parser import HTMLParser

class DepthParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = {}
        self.level = 0

    def handle_starttag(self, tag, attrs):
        self.tags.setdefault(self.level, set()).update([tag])
        self.level += 1

    def handle_endtag(self, tag):
        self.level -= 1

def solution(document):

    dp = DepthParser()
    dp.feed(document)
    return sorted(dp.tags[max(dp.tags.keys())])
