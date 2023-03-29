def solution(s):
    answer = True
    NumberOfP = s.count('p') + s.count('P')
    NumberOfY = s.count('y') + s.count('Y')
    if(NumberOfP != NumberOfY):
        answer = False
    
    return answer