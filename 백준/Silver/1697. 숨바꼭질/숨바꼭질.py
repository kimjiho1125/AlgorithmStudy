from collections import deque

def bfs(x): 
    queue = deque()
    queue.append(x)
    visited[x] = True
  
    while queue:
        x = queue.popleft()
        
        if x == k:
            return board[x]

        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= max_length and not visited[nx]:
                queue.append(nx)
                visited[nx] = True
                board[nx] = board[x] + 1

n, k = map(int, input().split())

#bfs 누적합으로 해봅시다
max_length = 100001
board = [0] * (max_length + 1)
visited = [False] * (max_length + 1)  
print(bfs(n))
