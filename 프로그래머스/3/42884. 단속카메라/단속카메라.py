def solution(routes):
    answer = 0
    last_camera = -30001
    
    routes.sort(key = lambda x : x[1])
    
    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]
        
    return answer