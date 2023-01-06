from collections import defaultdict
from html.parser import HTMLParser

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.stats = defaultdict(set)

    def handle_starttag(self, tag, attrs):
        self.stats[self.level].add(tag)
        self.level += 1

    def handle_endtag(self, tag):
        self.level -= 1

    def complexity(self):
        n = sorted(self.stats.keys())[-1]
        return sorted(self.stats[n])

def solution(document):
    p = Parser()
    p.feed(document)
    return p.complexity()
