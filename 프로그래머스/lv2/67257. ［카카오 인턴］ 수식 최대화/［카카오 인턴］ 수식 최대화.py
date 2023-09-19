from itertools import permutations
import re
import operator

def solution(expression):
    op = []
    prioritys = []
    answers = []
    
    #연산자 종류에 따른 연산
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    
    #연산자가 몇 종류인지 구하기
    for s in expression:
        if s in ['+','-','*'] and s not in op:
            op.append(s)
        #어차피 연산자의 최대 개수는 3이므로 뒤에는 볼 필요가 없음
        if len(op)==3:
            break
    
    #순열을 이용하여 주어진 연산자의 종류에 대해 모든 가능한 우선순위 구하기
    for i in permutations(op,len(op)):
        prioritys.append(i)
        
    #split을 이용하여 expression을 분리
    expression = re.split('([-|+|*])', expression)
    
    #우선순위 별로 계산 진행
    for priority in prioritys:
        ex = expression.copy()
        for opt in priority:
            while opt in ex:
                idx = ex.index(opt)
                temp = ops[ex.pop(idx)](int(ex.pop(idx-1)),int(ex.pop(idx-1)))
                ex.insert(idx-1, temp)
            
        if ex[0] not in answers:
            answers.append(abs(ex[0]))
    
    #최대값을 찾기 위해 역순으로 정렬
    answers.sort(reverse = True)
    
    return answers[0]