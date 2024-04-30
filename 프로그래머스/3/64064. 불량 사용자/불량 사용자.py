def solution(user_id, banned_id):
    answer = set()
    
    def check(u_id, b_id):
        if len(u_id) != len(b_id):
            return False
        
        for i in range(len(u_id)):
            if b_id[i] == '*':
                continue
            if b_id[i] != u_id[i]:
                return False
            
        return True
    
    def dfs(idx):
        if idx == len(banned_id):
            temp_list = []
            for i in range(len(visited)):
                if visited[i] == True:
                    temp_list.append(user_id[i])
            answer.add(tuple(temp_list))
            return
        
        for i in range(len(user_id)):
            if not visited[i] and check(user_id[i], banned_id[idx]):
                visited[i] = True
                dfs(idx + 1)
                visited[i] = False
                
    visited = [False] * len(user_id)
    dfs(0)
    
    return len(answer) 