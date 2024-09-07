from collections import deque

#bfs 메서드 정의
def bfs(board, start, visited):
  x,y = start
  queue = deque([start])
  #현재 좌표를 방문처리
  visited[x][y] = True
  #큐가 빌 때까지 반복
  while queue:
    x,y = queue.popleft()
    #해당 좌표에서 갈 수 있는 다음 좌표들을 큐에 삽입
    if x + board[x][y] < n and not visited[x + board[x][y]][y]:
      visited[x + board[x][y]][y] = True
      queue.append((x + board[x][y], y))
    if y + board[x][y] < n and not visited[x][y + board[x][y]]:
      visited[x][y + board[x][y]] = True
      queue.append((x, y + board[x][y]))

#게임 구역의 크기 N 입력받기
n = int(input())
board = []
visited = [[False] * n for _ in range(n) ]
#게임 구역 초기화
for _ in range(n):
  board.append(list(map(int, input().split())))

#bfs 함수 호출
bfs(board,(0,0), visited)

#결과 출력
if visited[n-1][n-1] == True:
  print("HaruHaru")
else:
  print("Hing")