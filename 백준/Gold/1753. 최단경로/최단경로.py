import heapq 
import sys

input = sys.stdin.readline
INF = int(1e9)

#정점의 개수, 간선의 개수 입력받기
V, E = map(int, input().split())

#시작 정점의 번호 입력받기
S = int(input())

#각 정점에 연결되어 있는 정점에 대한 정보를 담는 리스트 만들기
graph = [[] for _ in range(V + 1)]

#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (V + 1)

#모든 간선, 가중치 정보 입력받기
for _ in range(E):
  u, v, w = map(int, input().split())
  graph[u].append((v, w))

#다익스트라
def dijkstra(S):
  q = []
  #시작 노드로 가기 위한 가중치는 0으로 설정하여, 큐에 삽입
  heapq.heappush(q, (0, S))
  distance[S] = 0

  while q:
    w, now = heapq.heappop(q)
    if distance[now] < w:
      continue
    # 현재 정점과 연결된 다른 인접한 정점들 확인
    for i in graph[now]:
      cost = w + i[1]
      #현재 노드를 거쳐 다른 노드로 이동하는 거리다 더 짧은 경우
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

#다익스트라 알고리즘 수행
dijkstra(S)

#각 정점까지의 최단거리 출력
for i in range(1, V+1):
  if distance[i] == INF:
    print('INF')
  else:
    print(distance[i])