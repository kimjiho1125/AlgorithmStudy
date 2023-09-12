from collections import deque

#타입 판별 - 'A'이면 올바른 괄호 문자열 / 'B'이면 균형잡힌 괄호 문자열
def isType(p):
    letters = {'(': 0, ')': 0}
    stack = deque()
    
    for letter in p:
        if letter == '(':
            stack.append(letter)
            letters[letter] += 1
        elif letter == ')':
            if len(stack) == 0:
                return 'B'
            stack.pop()
            letters[letter] += 1
    
    if letters['('] == letters[')']:
        if len(stack) == 0:
            return 'A'
        else:
            return 'B'
    

def recursive(p):
    letters = {'(': 0, ')': 0}
    u = ''
    v = ''
    #입력이 빈 문자열이면 빈 문자열 반환
    if p == '':
        return ''
    
    #u,v 나누기
    for i,letter in enumerate(p):
        letters[letter] += 1
        #균형 잡힌 괄호 문자열이면
        if letters['('] == letters[')']:
            # u,v 분리하고 break
            u = p[:i+1]
            v = p[i+1:]
            break
    
    if isType(u) == 'A':
        s = recursive(v)
        return u + s
    else:
        #u 변경
        temp = ''
        u = list(u)
        del u[0]
        del u[-1]
        u = "".join(u)
        for i,letter in enumerate(u):
            if letter == '(':
                temp += ')'
            elif letter == ')':
                temp += '('
            
        return '(' + recursive(v) + ')' + temp

def solution(p):  
    return recursive(p)