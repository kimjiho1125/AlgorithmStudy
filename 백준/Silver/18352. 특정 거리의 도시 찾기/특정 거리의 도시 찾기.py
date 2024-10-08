import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append((b,1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            if dist+1 < distance[i[0]]:
                distance[i[0]] = dist+1
                heapq.heappush(q, (dist+1, i[0]))
        
dijkstra(x)

count = 0
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        count += 1
    if i == n and count == 0:
        print(-1)