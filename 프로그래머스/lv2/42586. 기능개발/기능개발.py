def solution(progresses, speeds):
    answer = []
    
    while len(progresses) > 0:
        temp = 0
        #진행한 만큼 더해준다
        for i,speed in enumerate(speeds):
            progresses[i] += speed
            
        #가장 앞에 있는 작업의 달성도가 100이 넘으면 그 뒤에 더 배포될 수 있는게 있는지 체크
        while progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            temp += 1
            if len(progresses) == 0:
                break
            
        #배포된게 있으면 정답 리스트에 추가
        if temp > 0:
            answer.append(temp)
            
    return answer