from collections import deque

def solution(begin, target, words):
    visited = dict()
    
    if target not in words:
        return 0
    
    def bfs(w,depth):
        queue = deque()
        queue.append((w,depth))
        visited[w] = True
        
        while queue:
            cur_word,cur_depth = queue.popleft()
            if cur_word == target:
                return cur_depth
            
            for word in words:
                cnt = 0
                if not visited[word]:
                    for i in range(len(word)):
                        if cnt > 1:
                            break
                        if cur_word[i] != word[i]:
                            cnt += 1
                    if cnt == 1:
                        queue.append((word,cur_depth + 1))
                        visited[word] = True
    
    #방문 여부를 표시할 딕셔너리 초기화
    for word in words:
        visited[word] = False
    
    answer = bfs(begin,0)
    
    
    return answer