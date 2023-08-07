from itertools import product

def solution(word):
    #중복 순열을 이용하여 모든 가능한 경우의 수 구하기
    cases = []
    letters = ['A','E','I','O','U']
    for i in range(1,6):
        for j in product(letters,repeat = i):
            cases.append(j)
    #사전 순서대로 정렬
    cases.sort()
    
    #입력받은 word를 튜플로 변경
    word = tuple(word)
    
    #순서를 리턴해준다
    return cases.index(word) + 1
        
    