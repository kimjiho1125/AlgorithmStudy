import sys

input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N)]
visited = [False] * N
root = 0
answer = 0

#노드 정보 입력받아서 tree 리스트에 부모-자식 관계 정보 저장
for node, parent in enumerate(map(int, input().split())):
  if parent == -1:
    root = node
  else:
    tree[parent].append(node)

#삭제 노드
delete_node = int(input())
#삭제 노드 방문 처리 => 이러면 탐색시 자식 노드 방문 X
visited[delete_node] = True

def dfs(start):
  global answer

  #방문 한적이 있다면 종료
  if visited[start]:
    return

  visited[start] = True

  if(len(tree[start]) == 0):
    answer += 1
  elif len(tree[start]) == 1 and tree[start][0] == delete_node:
    answer += 1
  else:
    for x in tree[start]:
      dfs(x)

dfs(root)
print(answer)