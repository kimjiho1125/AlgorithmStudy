import sys

#방향 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

input = sys.stdin.readline

N,K = map(int, input().split())

#바이러스들의 좌표 정보를 저장할 딕셔너리
virus = dict()
for i in range(1, K+1):
  virus[i] = []

#시험관 정보를 저장할 리스트
board = []

#시험관 정보 입력받기
for _ in range(N):
  board.append(list(map(int, input().split())))

#S, X, Y 입력받기
S, X, Y = map(int, input().split())

#딕셔너리에 바이러스들의 좌표를 저장
for i in range(N):
  for j in range(N):
    if board[i][j] != 0:
      virus[board[i][j]].append((i,j))

#S초 동안 바이러스 퍼트리기
for _ in range(S):
  for num in virus.keys():
    temp = virus[num].copy()

    for (x,y) in temp:
      count = 0
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
          count += 1
          board[nx][ny] = num
          if nx == X-1 and ny == Y-1:
            print(num)
            exit()
          virus[num].append((nx,ny))
      if count == 0:
        virus[num].remove((x,y))
      
#(X,Y)좌표에 존재하는 바이러스 번호 출력
print(board[X-1][Y-1])