from collections import deque

def solution(maps):
    n = len(maps) # y축
    m = len(maps[0]) # x축
    
    if n == 1 and m == 1:
        return 1
    
    #방향(순서대로 북 동 서 남)
    dx = [0,1,0,-1] 
    dy = [1,0,-1,0]
    
    # dfs => 효율성 측면에서 시간 초과 발생
    # def dfs(row,col,count):
    #     if maps[n-1][m-1] != 1 and count >= maps[n-1][m-1]:
    #         return
    #     maps[row][col] = count
    #     for x,y in zip(dx,dy):
    #         new_row = row + y
    #         new_col = col + x
    #         if new_col < 0 or new_col >= m or new_row < 0 or new_row >= n or maps[new_row][new_col] == 0 or (maps[new_row][new_col] != 1 and maps[new_row][new_col] <= count + 1):
    #             continue
    #         dfs(new_row,new_col,count+1)
    # dfs(0,0,1)
    # goal = maps[n-1][m-1]
    
    def bfs():
        queue = deque()
        queue.append((0,0))
        
        while queue:
            row,col = queue.popleft()
            # 목표 지점 도달시 리턴
            if (row,col) == (n-1,m-1):
                return maps[row][col]
            for (x,y) in zip(dx,dy):
                new_row = row + y
                new_col = col + x
                if new_row < 0 or new_row >= n or new_col < 0 or new_col >= m or maps[new_row][new_col] == 0 or (maps[new_row][new_col] != 1 and maps[new_row][new_col] <= maps[row][col] + 1):
                    continue
                maps[new_row][new_col] = maps[row][col] + 1
                queue.append((new_row,new_col))
        return -1
    
    return bfs()
            