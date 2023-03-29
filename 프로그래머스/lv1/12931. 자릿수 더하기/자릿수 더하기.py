def solution(n):
    answer = 0
    n = str(n)
    for i in range(len(n)):
        answer += int(n[i])
    
    print(answer)

    return answer