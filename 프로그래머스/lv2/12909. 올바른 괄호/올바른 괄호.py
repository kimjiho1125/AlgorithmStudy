def solution(s):
    temp = []
    for x in s:
        if x == "(":
            temp.append("(")
        elif x == ")":
            if len(temp) == 0:
                return False
            else:
                temp.pop()
            
    if len(temp) != 0:
        return False
    
    return True