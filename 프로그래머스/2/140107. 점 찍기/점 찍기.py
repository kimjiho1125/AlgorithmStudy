import math

def solution(k, d):
    answer = 0
    s = 0
    
    for y in range(0,d+1,k):
        xs = d**2 - y**2
        cnt = math.sqrt(xs) // k + 1
        s += cnt
    
    return s