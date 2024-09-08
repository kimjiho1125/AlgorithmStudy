from collections import deque

n,m = map(int, input().split())
maps = []
visited = [[False] * n for _ in range(m)]

for _ in range(m):
  maps.append(list(map(int, input().split())))

#이동 방향 동,남
dx = [0, 1]
dy = [1, 0]

def bfs(start):
  x, y = start
  queue = deque([start])
  visited[x][y] = True

  while queue:
    x, y = queue.popleft()

    for i in range(2):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < m and ny < n and maps[nx][ny] and not visited[nx][ny]:
        visited[nx][ny] = True
        queue.append((nx,ny))

bfs((0,0))

if visited[m-1][n-1]:
  print("Yes")
else:
  print("No")