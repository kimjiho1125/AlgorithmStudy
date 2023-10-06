import math

def gcd_N(arr):
    gcd = arr[0]
    for item in arr:
        gcd = math.gcd(gcd,item)
    return gcd

def solution(arrayA, arrayB):
    answer = 0
    #arrayA의 최대공약수 구하기
    answer = gcd_N(arrayA)
    if answer != 0:
        #arrayA의 최대공약수가 존재한다면 arrayB의 숫자들을 나눠본다
        for item in arrayB:
            if item%answer == 0:
                answer = 0
                break
        
    #반대로도 한번 진행한다
    answer2 = gcd_N(arrayB)
    if answer2 != 0:
        #arrayB의 최대공약수를 이용하여 arrayA의 숫자들을 나눈다
        for item in arrayA:
            if item%answer2 == 0:
                answer2 = 0
                break
    
    return max(answer,answer2)