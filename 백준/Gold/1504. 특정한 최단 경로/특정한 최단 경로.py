import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

#정점의 개수 N과 간선의 개수 E 입력받기
N, E = map(int, input().split())
#각 정점에 연결되어 있는 정점들의 연결 정보를 담는 리스트
graph = [[] for _ in range(N+1)]
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (N+1)
#모든 간선, 거리 입력받기
for _ in range(E):
  a,b,c = map(int, input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))

#통과해야 하는 정점 입력받기
v1, v2 = map(int, input().split())

def dijkstra(S):
  q = []
  heapq.heappush(q, (0,S))
  distance[S] = 0

  while q:
    dist, now = heapq.heappop(q)
    #이미 처리했다면 패스
    if distance[now] < dist:
      continue
    #현재 정점과 연결된 인접한 정점들 확인
    for i in graph[now]:
      cost = distance[now] + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))

dijkstra(1)
result1 = distance[v1]
result2 = distance[v2]
distance = [INF] * (N+1)

dijkstra(v1)
result1 += distance[v2]
result2 += distance[N]
distance = [INF] * (N+1)

dijkstra(v2)
result1 += distance[N]
result2 += distance[v1]

result = min(result1, result2)
if result >= INF:
  print(-1)
else:
  print(result)