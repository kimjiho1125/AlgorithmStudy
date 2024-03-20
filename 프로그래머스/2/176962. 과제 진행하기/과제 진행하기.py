def solution(plans):
    answer = []
    stop_plans = [] #멈춰둔 과제를 저장
    
    #start를 분으로 변환 and playtime 정수로 변환
    def start_to_min(plans):
        for plan in plans:
            minute = int(plan[1][0:2])*60 + int(plan[1][3:])
            plan[1] = minute
            plan[2] = int(plan[2])
    
    #시작 시각 분으로 변환
    start_to_min(plans)
    
    #시작 시간을 기준으로 정렬
    plans.sort(key = lambda x : x[1])
    
    #일단 한 바퀴 돌려서 시간 안에 끝낼 수 있는 건 끝내서 answer에 넣고 못 끝내는건 stop_plans배열에 넣기
    for i in range(len(plans)):
        if i == len(plans) - 1:
            answer.append(plans[i][0])
            break
        
        available_time = plans[i+1][1] - plans[i][1]
        if available_time >= plans[i][2]:
            available_time -= plans[i][2]
            answer.append(plans[i][0])
    
            while available_time > 0 and stop_plans:
                new_plan = stop_plans.pop()
                if available_time >= new_plan[2]:
                    available_time -= new_plan[2]
                    answer.append(new_plan[0])
                elif available_time < new_plan[2]:
                    new_plan[2] -= available_time
                    stop_plans.append(new_plan)
                    break
            
        else:
            plans[i][2] -= available_time
            stop_plans.append(plans[i])
        
    #stop_plans에 있는거 나중에 들어온 순서대로 answer에 넣기
    for _ in range(len(stop_plans)):
        answer.append(stop_plans.pop()[0])
            
    return answer