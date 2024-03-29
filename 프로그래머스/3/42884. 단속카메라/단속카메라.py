def solution(routes):
    answer = 0
    len_routes = len(routes)
    routes.sort(key = lambda x : (x[0],x[1]))
    i = 1
    cm_start, cm_last = routes[0]
    
    while i < len_routes:
        
        start, last = routes[i]
        
        if cm_last >= start:
            cm_start = start
            if cm_last > last:
                cm_last = last
        else:
            answer += 1
            cm_start, cm_last = start, last
        i += 1
        if i == len_routes - 1:
            answer += 1
        
    return answer