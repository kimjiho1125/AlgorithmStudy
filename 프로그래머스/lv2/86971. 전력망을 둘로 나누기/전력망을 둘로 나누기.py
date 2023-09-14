from collections import deque

def dfs(wires,start_node):
    visited = []
    need_visited = deque()
    
    #시작 노드 설정
    need_visited.append(start_node)
    
    #방문이 필요한 노드가 아직 존재 한다면
    while need_visited:
        #시작 노드 설정
        node = need_visited.pop()
        
        #만약 방문한 리스트에 해당 노드가 없다면
        if node not in visited:
            #방문한 리스트에 해당 노드 추가
            visited.append(node)
            #인접 노드들을 방문 예정 리스트에 추가
            for wire in wires:
                if node == wire[0] and wire[1] not in visited:
                    need_visited.append(wire[1])
                if node == wire[1] and wire[0] not in visited:
                    need_visited.append(wire[0])
    return len(visited)

def solution(n, wires):
    mins = []
    
    for i in range(len(wires)):
        copy_wires = wires.copy()
        copy_wires.pop(i)
        num1 = dfs(copy_wires,1)
        num2 = n-num1
        mins.append(abs(num1-num2))
    
    mins.sort()
    
    return mins[0]