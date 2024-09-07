from collections import deque

def bfs(start):
  queue = deque([(start, 0)])
  visited[start] = True

  while queue:
    num, cnt = queue.popleft()

    if num == k:
      return cnt

    for i in [num + 1, num * 2]:
      if not visited[i] and i <= k:
        visited[i] = True
        queue.append((i, cnt + 1))

a, k = map(int, input().split())
visited = [False] * (k*2 + 1)
print(bfs(a))