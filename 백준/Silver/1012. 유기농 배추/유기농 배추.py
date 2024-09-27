from collections import deque
#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(board, visited, start):
    q = deque([start])
    visited[start[0]][start[1]] = True
    
    while q:
        x,y = q.popleft()
        

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
    

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    board = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    count = 0
    for _ in range(K):
        y,x = map(int, input().split())
        board[x][y] = 1
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and not visited[i][j]:
                bfs(board, visited, (i,j))
                count += 1

    print(count)