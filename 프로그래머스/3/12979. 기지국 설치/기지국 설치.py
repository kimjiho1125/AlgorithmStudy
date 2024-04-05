import math
        
def solution(n, stations, w):
    answer = 0
    r = 2 * w + 1
    start = 1
    
    for station in stations:
        if station - w - start > 0 :
            answer += math.ceil((station - w - start) / r)
        start = station + w + 1
    
    if n - start + 1 > 0:
        answer += math.ceil((n - start + 1) / r)
    
    return answer