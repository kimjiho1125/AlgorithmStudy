import math 

def solution(n, k):
    
    numbers = [i for i in range(1,n+1)]
    answer = []
    
    while n > 0:
        idx = (k-1) // math.factorial(n-1)
        answer.append(numbers.pop(idx))
        k = k % math.factorial(n-1)
        n -= 1
    
    return answer