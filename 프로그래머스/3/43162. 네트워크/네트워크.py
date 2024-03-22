from collections import deque

def solution(n, computers):
    #방문 여부를 표시할 리스트
    visited = [False] * n
    #네트워크의 개수
    count = 0
    
    #bfs
    def bfs(v):
        queue = deque([v])
        
        while queue:
            v = queue.popleft()
            visited[v] = True
            
            for i in range(n):
                #자기 자신이면 무시
                if i == v:
                    continue
                #v의 인접노드이면 queue에 추가하고 방문처리
                elif computers[v][i] == 1:
                    if visited[i] == False:
                        queue.append(i)
                
    for v in range(n):
         if not visited[v]:
            bfs(v)
            count += 1
                
    return count