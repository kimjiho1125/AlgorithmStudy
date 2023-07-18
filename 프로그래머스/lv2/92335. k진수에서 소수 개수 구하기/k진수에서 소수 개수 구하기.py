import math

def is_prime(x):
    if x == 1:
        return False
    #2부터 x의 제곱근 까지의 모든 수를 확인
    for i in range(2,int(math.sqrt(x)) + 1):
        #x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            #소수가 아니다
            return False
    #나누어 떨어지는 경우가 하나도 없다면 소수
    return True

def change(n,k):
    rev_base = ''
    
    while n > 0:
        n, mod = divmod(n,k)
        rev_base += str(mod)
    
    return rev_base[::-1]

def solution(n, k):
    answer = 0
    #n을 k진수로 변환
    changed_number = change(n,k)
    #0을 기준으로 숫자들을 분리 => 10진수 취급
    candidates = changed_number.split('0')
    #컴프리헨션을 사용하여 빈 문자열들 제거
    candidates = [i for i in candidates if i != '']
    #소수 판별
    for candidate in candidates:
        isPrime = is_prime(int(candidate))
        if isPrime == True:
            answer += 1
        
    return answer