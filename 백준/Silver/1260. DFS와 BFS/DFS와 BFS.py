import sys
from collections import deque

def dfs(v):
    visited[v] = True
    print(v, end = " ")
    for x,y in graph:
        if x == v and not visited[y]:
            dfs(y)

def bfs(v):
    queue = deque()
    visited[v] = True
    queue.append(v)
    print(v,end=" ")

    while queue:
        node = queue.popleft()

        for x,y in graph:
            if x == node and not visited[y]:
                queue.append(y)
                visited[y] = True
                print(y, end = " ")

n, m, v = map(int, sys.stdin.readline().split())
graph = []
visited = [False] * (n+1)


for _ in range(m):
    x,y = map(int, sys.stdin.readline().split())
    graph.append((x,y))
    graph.append((y,x))

#graph정렬
graph.sort(key = lambda x: (x[0], x[1]))

dfs(v)
print()
visited = [False] * (n+1)
bfs(v)
