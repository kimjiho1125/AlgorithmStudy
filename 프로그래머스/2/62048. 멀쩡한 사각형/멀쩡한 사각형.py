import math

def solution(w,h):
    total = w * h
    removed = w + h - math.gcd(w,h)
    return total - removed