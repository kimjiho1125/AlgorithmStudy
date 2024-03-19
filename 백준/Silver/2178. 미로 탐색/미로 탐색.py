import sys
from collections import deque

#각종 초기화   
n,m = map(int, sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]
visited=[[False for _ in range(m)] for _ in range(n)]

#상하좌우
dy = [-1,0,1,0]
dx = [0,1,0,-1]

def bfs(x,y):
    #queue를 구현하기 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    #현재 좌표를 방문처리
    visited[x][y] = True
    #queue가 빌때까지 반복
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1 and visited[nx][ny] == False:
                queue.append((nx,ny))
                visited[nx][ny] = True
                board[nx][ny] = board[x][y] + 1

    return board[n-1][m-1]

print(bfs(0,0))