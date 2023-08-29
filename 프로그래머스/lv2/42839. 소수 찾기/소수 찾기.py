from itertools import permutations
import math

def is_prime_number(x):
    #2부터 x의 제곱근 까지 모든 수를 확인
    for i in range(2,int(math.sqrt(x)) + 1):
        #x가 해당 수로 나누어 떨어지면 소수 아님
        if x % i == 0:
            return False
    return True
    
def solution(numbers):
    answer = 0
    numbers = list(numbers)
    all_num = []
    result = []
    #모든 경우의 수 구하기
    for i in range(1,len(numbers) + 1):
        temp = list(permutations(numbers,i))
        all_num += temp
        
    #중복 제거  
    all_num = list(set(all_num))
    
    for num in all_num:
        num = int("".join(num))
        if num > 1:
            result.append(num)
            
    #중복 제거    
    result = list(set(result))
    
    #소수 판별
    for x in result:
        if is_prime_number(x):
            answer += 1
            
    return answer