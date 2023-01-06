from urllib.parse import urlparse, parse_qs
from itertools import takewhile

def solution(url1, url2):

    pr1 = urlparse(url1)
    pr2 = urlparse(url2)
    score = (pr1.scheme == pr2.scheme) * 5 + (pr1.netloc == pr2.netloc) * 10

    p1 = pr1.path.split('/')[1:]
    p2 = pr2.path.split('/')[1:]
    score += len(list(takewhile(lambda x: x[0] == x[1], zip(p1, p2))))

    q1 = parse_qs(pr1.query)
    q2 = parse_qs(pr2.query)
    score += sum(2 if q1[key] == q2[key] else 1 for key in q1.keys() & q2.keys())

    return score
