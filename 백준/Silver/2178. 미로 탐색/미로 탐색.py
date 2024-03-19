#1 이동 가능 / 0 이동 불가
#(1,1) 출발 (N,M) 도착할때 걸리는 '최소' 칸수 => BFS구나 방법은 누적합 구하기
#입력 : 첫째 줄: n,m 둘째줄부터는 미로
import sys
from collections import deque

#동서남북
dy = [-1,0,1,0]
dx = [0,1,0,-1]

#초기화
n,m = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)] #readline을 쓸 경우 줄바꿈 문자까지 포함. 따라서 rstrip을 사용하여 줄바꿈 문자를 제거
visited = [[False for _ in range(m)] for _ in range(n)]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #해당 좌표가 방문 가능한 좌표인지 체크
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1 and visited[nx][ny] != True:
                #이동 가능하면 방문 체크, 이동 거리 갱신
                queue.append((nx,ny))
                visited[nx][ny] = True
                board[nx][ny] = board[x][y] + 1

    return board[n-1][m-1]

print(bfs(0,0))
