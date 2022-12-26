from math import gcd
import functools

def solution(denominators):
    return functools.reduce(lambda x, y: x*y//gcd(x, y), denominators)
