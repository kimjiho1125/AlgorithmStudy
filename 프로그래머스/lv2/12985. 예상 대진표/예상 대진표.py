def solution(n,a,b):
    currentRound = 1
    
    #정렬
    if a>b:
        a,b = b,a
    
    while (a%2 == 0 or a+1 != b):
        #라운드 수를 +1한다
        currentRound += 1
        
        #a,b가 짝수인지 홀수인지 판별하여 다음 라운드의 순서를 배정한다.
        if a % 2 != 0:
            a = a + 1
        if b % 2 != 0:
            b = b + 1
        a /= 2
        b /= 2
            
    return currentRound