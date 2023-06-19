def solution(n):
    
    # 답이 피보나치 수열임을 알아차리는게 포인트 
    currentNum = 1
    nextNum = 2
    
    if n == 1:
        return currentNum
    elif n == 2:
        return nextNum
    
    else:
        for i in range(n-1):
            currentNum, nextNum = nextNum, currentNum + nextNum
        
    return currentNum % 1234567