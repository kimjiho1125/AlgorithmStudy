from collections import deque

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
my_score = 0
e_score = 0
# 방문 여부를 저장할 변수
visited = [[False] * n for _ in range(m)]
# 전장 상황을 저장할 변수
board = [list(input()) for _ in range(m)]


def bfs(x, y, color):
    q = deque([(x, y)])
    cnt = 1
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == color:
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += 1

    return pow(cnt,2)

for i in range(m):
  for j in range(n):
    if not visited[i][j] and board[i][j] == "W":
      my_score += bfs(i, j, "W")
    if not visited[i][j] and board[i][j] == "B":
      e_score += bfs(i, j, "B")

print(my_score, e_score, sep=" ")        