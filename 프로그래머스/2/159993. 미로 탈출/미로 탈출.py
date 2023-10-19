from collections import deque
   
def solution(maps):
    n = len(maps) #y축
    m = len(maps[0])#x축
    
    #서 북 동 남
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    def bfs(start,end):
        #초기화
        visit = [[0 for _ in range(m)] for _ in range(n)]
        queue = deque()
        queue.append(start)
        
        while queue:
            x,y = queue.popleft()
            
            for i in range(4):
                xx, yy = x + dx[i], y + dy[i]
                if 0 <= xx < n and 0 <= yy < m and not visit[xx][yy] and maps[xx][yy] != "X":
                    visit[xx][yy] = visit[x][y] + 1
                    queue.append((xx,yy))
                
        return visit[end[0]][end[1]]
    
    #출발점, 레버, 출구 좌표 구하기
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                start = (i,j)
            elif maps[i][j] == "L":
                lever = (i,j)
            elif maps[i][j] == "E":
                exit = (i,j)
    
    d1 = bfs(start,lever)
    d2 = bfs(lever,exit)
    
    return d1 + d2 if d1 and d2 else -1