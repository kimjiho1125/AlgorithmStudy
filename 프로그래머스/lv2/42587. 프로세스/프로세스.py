def solution(priorities, location):
    answer = 0
    locations = [0 for _ in range(len(priorities))]
    locations[location] = 1
    while len(priorities) > 0:
        maxNum = max(priorities)
        priority = priorities.pop(0)
        loca = locations.pop(0)
        if maxNum <= priority:
            answer += 1
            if loca == 1:
                return answer
        else:
            priorities.append(priority)
            locations.append(loca)
            
            
        
    
    
    
    
    