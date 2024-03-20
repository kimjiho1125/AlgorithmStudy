result = 0

def solution(n):
    #1차원 리스트로 board를 표현 index => row / value => column
    board = [0] * n
    visited = [False] * n
                    
    def dfs(depth): 
        global result
        
        #depth == n이면 모든 퀸을 다 놓은 것
        if depth == n:
            result += 1
            return
        
        #해당 depth에서 놓을 수 있는 column을 고른다.
        for i in range(n):
            
            if not visited[i]:
                board[depth] = i #해당 depth의 i번째 컬럼에 퀸을 둔다
                
                if check(depth):
                    visited[i] = True # 해당 열 방문 처리
                    dfs(depth+1) #다음 depth로 넘어감
                    visited[i] = False # 해당 열 다시 방문X => 여기 까지 왔다는 거는 이후 불가능하단 소리
                
    
    def check(current_depth):
        for i in range(current_depth):
            if (board[i] == board[current_depth] or (current_depth - i == abs(board[i] - board[current_depth]))):
                return False
        return True
    
    
    dfs(0)
    
    return result