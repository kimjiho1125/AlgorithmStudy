from collections import deque

def solution(edges):
    
    def count_edges(edges):
        edges_counts = {}
        for a, b in edges:
            
            if a not in edges_counts:
                edges_counts[a] = [0,0]
            if b not in edges_counts:
                edges_counts[b] = [0,0]
            
            edges_counts[a][0] += 1
            edges_counts[b][1] += 1
            
        return edges_counts
    
    def check_answer(edges_counts):
        answer = [0, 0, 0, 0]
        for key, counts in edges_counts.items():
            #정점 구하기 : 나가는 간선 수가 2개 이상, 들어오는 간선 수가 0개
            if counts[0] > 1 and counts[1] == 0:
                answer[0] = key
            #막대 그래프 구하기 : 나가는 간선 수가 0개, 들어오는 간선 수가 1개 이상인 노드의 개수와 같음
            elif counts[0] == 0 and counts[1] > 0:
                answer[2] += 1
            #8자 그래프 개수 : 나가는 간선 수가 2개, 들어오는 간선 수가 2개 이상인 노드의 개수와 같음
            elif counts[0] == 2 and counts[1] >= 2:
                answer[3] += 1
            
        answer[1] = (edges_counts[answer[0]][0] - answer[2] - answer[3])
        
        return answer
        
    edges_counts = count_edges(edges)
    answer = check_answer(edges_counts)
        
    return answer
        