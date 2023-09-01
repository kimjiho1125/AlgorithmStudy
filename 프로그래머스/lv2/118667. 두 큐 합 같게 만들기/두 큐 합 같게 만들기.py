from collections import deque

def solution(queue1, queue2):
    #시간 효율성을 위해 list => deque로 변경
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    #sum함수 사용을 최소화하여 시간을 줄이기 위해 변수 사용
    q1s = sum(queue1)
    q2s = sum(queue2)
    
    total = q1s + q2s
    
    #종료조건1 -- 홀수의 경우 반반 불가능
    if total % 2 == 1:
        return -1
    
    #종료조건2 -- 큐의 원소의 개수들의 합 초과
    limit = len(queue1) + len(queue2)
    
    count = 0
    
    #같아지도록 작업 -- 원소의 합이 큰 큐에서 원소의 합이 작은 큐로 원소를 옮긴다
    while q1s != q2s:
        
        if count >= limit:
            return -1
        
        while queue2 and q1s < q2s:
            tmp = queue2.popleft()
            queue1.append(tmp)
            count += 1
            q1s += tmp
            q2s -= tmp
        
        while queue1 and q1s > q2s:
            tmp = queue1.popleft()
            queue2.append(tmp)
            count += 1
            q2s += tmp
            q1s -= tmp
            
    return count