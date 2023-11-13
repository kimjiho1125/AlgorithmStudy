import heapq

def dijkstra(road, N, K):
    #최종적으로 정답을 저장할 변수
    answer = 0
    #시작점으로부터의 거리를 저장할 배열 distance 초기화
    distance = [float("inf") for _ in range(N+1)]
    distance[1] = 0
    #노드들의 연결 관계에 대한 정보를 저장한 graph 배열 초기화
    graph = [[] for _ in range(N+1)]
    for start,end,cost in road:
        graph[start].append([end,cost])
        graph[end].append([start,cost])
    #heap에 시작점의 cost, 시작 노드 정보 넣기
    heap = []
    heapq.heappush(heap,(distance[1],1))
    
    #heap이 비어질때까지 다익스트라 알고리즘을 반복
    while heap:
        cost, current_node = heapq.heappop(heap)
        if distance[current_node] < cost:
            continue
        for next_node, c in graph[current_node]:
            total_cost = cost + c
            if total_cost < distance[next_node]:
                distance[next_node] = total_cost
                heapq.heappush(heap,[total_cost,next_node])
    #total_cost가 K이하인 노드의 개수 찾기
    for c in distance:
        if c <= K:
            answer += 1
    #정답 리턴
    return answer
    
def solution(N, road, K):
    return dijkstra(road,N,K)