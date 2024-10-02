import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n+1)]
visited = [0] * (n+1)
stack = []

#두 정점의 연결 정보를 업데이트
for _ in range(n-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

#DFS 알고리즘
def dfs(start):
  stack.append(start)

  while stack:
    target = stack.pop()
    for i in graph[target]:
      if not visited[i]:
        visited[i] = target
        stack.append(i)

dfs(1)

for i in range(2, n+1):
  print(visited[i])