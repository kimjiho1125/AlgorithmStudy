def solution(n):
    count = 1
    n -= count
    answer = 1
    while(n>0):
        count += 1
        n -= count
        if(n%count == 0):
            answer += 1
            
    return answer