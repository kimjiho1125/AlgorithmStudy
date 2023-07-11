import heapq

# 문제의 핵심 포인트! => 정렬 이후에 데이터가 추가되어도 계속 정렬된 상태를 유지해야함 => heapq 사용

def solution(scoville, K):
    count = 0
    # 정렬 이후에 데이터가 추가 되어도 계속 정렬된 상태를 유지하기 위해 heapq를 사용!
    heapq.heapify(scoville)
    
    if scoville[0] >= K:
        return count
    
    while scoville[0] < K:
        temp = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville,temp)
        count += 1
        
        if len(scoville) == 1:
            if scoville[0] > K:
                break
            else:
                return -1
    return count