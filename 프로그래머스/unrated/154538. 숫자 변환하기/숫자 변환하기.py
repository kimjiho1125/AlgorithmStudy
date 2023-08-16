from collections import deque

def dp(x, y, n, dist):
    queue = deque()
    dist[x] = 1
    queue.append(x)
    
    while queue:
        current = queue.popleft()
        
        if 0 <= current + n <= 1000000 and dist[current + n] == 0:
            dist[current + n] = dist[current] + 1
            queue.append(current + n)
        if 0 <= current * 2 <= 1000000 and dist[current * 2] == 0:
            dist[current * 2] = dist[current] + 1
            queue.append(current * 2)
        if 0 <= current * 3 <= 1000000 and dist[current * 3] == 0:
            dist[current * 3] = dist[current] + 1
            queue.append(current * 3)
        
def solution(x, y, n):
    # +1을 한 이유는 직관적으로 인덱스와 값을 일치시키기 위해서
    dist = [0] * 1000001
    dp(x,y,n,dist)
    return dist[y] - 1