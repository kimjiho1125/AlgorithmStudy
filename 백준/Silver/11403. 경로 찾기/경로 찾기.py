import sys

input = sys.stdin.readline
INF = int(1e9)

#정점의 개수 입력받기
n = int(input())
#각 간선에 대한 정보를 입력받아, 그 값으로 초기화
graph = [list(map(int, input().split())) for _ in range(n)]

#점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][k] and graph[k][b]:
                graph[a][b] = 1

#결과 출력
for g in graph:
    print(*g)