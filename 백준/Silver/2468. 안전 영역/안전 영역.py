import sys
from collections import deque

n = int(sys.stdin.readline())
board = []
max_len = 0
result = 0

#board 초기화 및 최대높이 찾기
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
    for j in range(n):
        if board[i][j] > max_len:
            max_len = board[i][j]

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def bfs(x,y,rain_length):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > rain_length and not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = True


#높이가 1일때부터 100일때까지 모든 경우의 수 구하기
for rain_length in range(max_len):
    visited = [[False for _ in range(n)] for _ in range(n)] #방문여부
    count = 0 #안전 지대 수

    #안전지대 체크
    for i in range(n):
        for j in range(n):
            if board[i][j] > rain_length and not visited[i][j]:
                bfs(i,j,rain_length)
                count += 1

    #안전지대 수 업데이트
    result = count if count > result else result


print(result)