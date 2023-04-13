def solution(k, m, score):
    answer = 0
    count = 0
    
    score.sort(reverse = True)
    for i in range((len(score)//m)*m):
        count += 1
        if count % m == 0:
            answer += score[i]*m
    return answer
        