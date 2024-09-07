def dfs(board, start, visited):
  stack = [(start)]
  x,y = start
  visited[x][y] = True

  while stack:
    x,y = stack.pop()
    if x + board[x][y] < n and not visited[x + board[x][y]][y]:
      visited[x + board[x][y]][y] = True
      stack.append((x + board[x][y], y))
    if y + board[x][y] < n and not visited[x][y + board[x][y]]:
      visited[x][y + board[x][y]] = True
      stack.append((x, y + board[x][y]))

n = int(input())
board=[]
visited = [[False] * n for _ in range(n)]

#board 초기화
for _ in range(n):
  board.append(list(map(int, input().split())))

#dfs 함수 호출
dfs(board, (0,0), visited)

#결과 출력
if visited[n-1][n-1] == True:
  print("HaruHaru")
else:
  print("Hing")