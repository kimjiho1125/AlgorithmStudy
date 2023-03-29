def solution(x, n):
    answer = []
    temp = 0
    for _ in range(n):
        temp += x
        answer.append(temp)
        
    return answer