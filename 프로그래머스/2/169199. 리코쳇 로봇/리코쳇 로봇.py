from collections import deque

def solution(board):
    start_pos = (0,0)
    goal_pos = (0,0)
    stack = deque()
    
    #보드 크기 구하기
    row = len(board)
    col = len(board[0])
    
    #방문 여부
    visit = [[False]*col for _ in range(row)]
    
    #방향 - 상 하 좌 우
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    #시작 위치, 목표 위치 찾기
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'R':
                start_pos = (i,j)
                stack.append((i,j,0))
            elif board[i][j] == 'G':
                goal_pos = (i,j)
                
#     #bfs로 최소 횟수 구하기
    while stack:
        current_pos = stack.popleft()
        visit[current_pos[0]][current_pos[1]] = True
        if (current_pos[0],current_pos[1]) == goal_pos:
            return current_pos[2]
        for i in range(4):
            add = 1
            yy = current_pos[0] + dy[i]
            xx = current_pos[1] + dx[i]
            #해당 방향으로 갈 수 있는 끝까지 가기
            while (0 <= xx < col and 0 <= yy < row and board[yy][xx] != 'D'):
                add += 1
                yy = current_pos[0] + dy[i] * add 
                xx = current_pos[1] + dx[i] * add   
            yy = current_pos[0] + dy[i] * (add-1)
            xx = current_pos[1] + dx[i] * (add-1)
            
            if not visit[yy][xx] and (current_pos[0],current_pos[1]) != (yy,xx):
                stack.append((yy,xx,current_pos[2] + 1))
                visit[yy][xx] = True
    
    return -1