import heapq

def solution(n, works):
    answer = 0
    time = n
    
    #해야할 일보다 남은 시간이 더 많은 경우 0리턴
    if n >= sum(works):
        return 0
    
    #maxheap처럼 사용하기 위해 전부 -1 곱해줌
    works = [-work for work in works]
    
    #max-heap 생성
    heapq.heapify(works)
    #최대값 pop해서 1빼고 다시 정렬 반복
    for _ in range(n):
        i = heapq.heappop(works)
        i += 1
        heapq.heappush(works,i)
    
    #야근 지수 구하기
    for work in works:
        answer += (work ** 2)
    
    return answer