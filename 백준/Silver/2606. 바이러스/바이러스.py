from collections import deque

num = int(input())
m = int(input())
graph = []
visited = [False] * (num + 1)

for m in range(m):
    graph.append(list(map(int,input().split())))

def bfs(node):
    queue = deque()
    queue.append(node)
    count = 0
    
    while queue:
        cur_node = queue.popleft()
        visited[cur_node] = True

        for [n1, n2] in graph:
            if n1 == cur_node and not visited[n2]:
                queue.append(n2)
                visited[n2] = True
                count += 1
            elif n2 == cur_node and not visited[n1]:
                queue.append(n1)
                visited[n1] = True
                count += 1              
    return count

print(bfs(1))