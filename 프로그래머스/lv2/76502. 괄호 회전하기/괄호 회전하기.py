# 회전 -> deque의 rotate함수를 떠올리면 된다!
# 올바른 괄호 규칙 관련해서 문제가 나오면 -> () {} [] 각각 빈문자열로 바뀌게 설정한 뒤 전체 문자열의 길이가 0인지 체크해주면 쉽게 체크할 수 있다.

from collections import deque 

def check(s):
    while True:
        if "()" in s: s = s.replace("()","")
        elif "{}" in s: s = s.replace("{}","")
        elif "[]" in s: s = s.replace("[]","")
        else: 
            return False if s else True
    
def solution(s):
    answer = 0
    dque = deque(s)
    
    for i in range(len(s)):
        if check(''.join(dque)): answer += 1
        dque.rotate(-1)
            
    return answer