import sys
sys.setrecursionlimit(10**7)

t = int(sys.stdin.readline()) # 테스트 케이스의 개수

def dfs(v):
    visited[v] = True #현재 노드 방문 처리
    nv = graph[v] #인접 노드
    if not visited[nv]: #인접 노드가 방문하지 않은 노드라면
        dfs(nv) 

for _ in range(t):
    n = int(sys.stdin.readline()) # 순열의 크기
    graph = list(map(int,sys.stdin.readline().split())) #순열
    graph.insert(0,0)
    visited = [False] * (n+1) # 1~n까지 사용
    cycle = 0 #순열 사이클의 개수

    for i in range(1,n+1):
        #방문하지 않은 노드라면
        if not visited[i]:
            dfs(i) #i번째 노드에서 dfs호출
            cycle += 1 #사이클 개수 +1
    
    print(cycle)