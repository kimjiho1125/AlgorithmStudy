def solution(n):
    answer = ''
    while n > 0:
        #n을 3으로 나눈 나머지가 0이 아니면
        #일반적인 3진법 변환과 동일함
        if n % 3:
            answer = str(n % 3) + answer
            n //= 3
        else:  
            answer = '4' + answer
            n = n//3 - 1
    return answer