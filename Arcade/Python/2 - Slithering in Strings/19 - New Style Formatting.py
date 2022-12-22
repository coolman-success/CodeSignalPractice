import re


def solution(s):
    s = re.sub("%%", "{%}", s)
    s = re.sub("%[bcdeEfFgGnosxX]", "{}", s)
    return re.sub("{%}", "%", s)
