import sys
from collections import deque

input = sys.stdin.readline

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#bfs
def bfs(visited, x, y, h):
  global res

  #수영장 될 수 있는지 여부를 판별
  flag = True
  #채울 수 있는 물의 양
  cnt = 1

  #bfs알고리즘
  queue = deque([(x, y)])
  visited[x][y] = True

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      #범위 밖으로 벗어나면 수영장이 될 수 없음
      if nx == -1 or nx == N or ny == -1 or ny == M:
        flag = False
        continue
      #수영장이 될 가능성이 있는 경우
      if board[nx][ny] <= h and not visited[nx][ny]:
        visited[nx][ny] = True
        queue.append((nx, ny))
        cnt += 1

  #수영장이 될 수 있다면      
  if flag:
    res += cnt

#총 수영장 물
res = 0
#수영장 만들 곳
board = []

N,M = map(int, input().split())

#수영장 만들 곳 초기화
for _ in range(N):
  board.append(list(map(int, list(input().rstrip()))))

#수위를 올려가며 수영장의 물이 담길 양을 구한다
for num in range(1,9):
  visited = [[0] * M for _ in range(N)]
  for i in range(N):
    for j in range(M):
      #현재 수면 보다 낮고 아직 체크하지 않은 곳이라면
      if board[i][j] <= num and not visited[i][j]:
        bfs(visited, i, j, num)

print(res)