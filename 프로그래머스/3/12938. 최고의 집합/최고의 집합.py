def solution(n, s):
    answer = []
    
    #원소의 수가 합보다 크면 불가능
    if n > s:
        return [-1]
    
    num, rest = divmod(s,n)
    
    for _ in range(n):
        answer.append(num)
    
    if rest > 0:
        for i in range(n-1,-1,-1):
            answer[i] += 1
            rest -= 1
            #종료 조건
            if rest == 0:
                break
    
    return answer