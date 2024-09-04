import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
graph = []

#각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(n):
    temp = list(map(int, input().split()))
    for i in range(n):
        if temp[i] == 0:
            temp[i] = INF
    graph.append(temp)

#점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

#수행된 결과를 출력
for a in range(n):
    for b in range(n):
        if graph[a][b] < INF:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()