from collections import Counter

def solution(weights):
    answer = 0
    counter = Counter(weights)
    
    #가능한 몸무게 범위를 모두 돌린다
    for i in range(100,1001):
        #현재 보고있는 몸무게가 주어진 몸무게 목록에 존재한다면
        if counter[i] > 0:
            #같은 몸무게가 존재하는지 체크
            answer += counter[i] * (counter[i] - 1) // 2
            #2:3 비율이 존재하는지 체크
            answer += counter[i] * (counter[i*3/2])
            #2:4 비율이 존재하는지 체크
            answer += counter[i] * (counter[i*2])
            #3:4 비율이 존재하는지 체크
            answer += counter[i] * (counter[i*4/3])
    
    return answer