#최소 신장 트리를 찾는 문제 => 크루스칼 알고리즘 사용
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    answer = 0
    #부모 테이블 초기화
    parent = [i for i in range(n)]
    
    #간선 정보를 비용 기준으로 오름차순으로 정렬
    costs.sort(key = lambda x: x[2])
    for i in range(len(costs)):
        a, b, cost = costs[i]
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost
        
    return answer