import heapq

def solution(scoville, K):
    count = 0
    # 정렬에서의 효율성을 향상시키기 위해 heapq를 사용!
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