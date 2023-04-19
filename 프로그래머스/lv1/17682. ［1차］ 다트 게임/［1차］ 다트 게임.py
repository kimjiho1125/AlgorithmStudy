def solution(dartResult):
    answer = 0
    count = 0
    temp = []
    i = 0
    while i < len(dartResult):
        if dartResult[i].isdigit():
            if dartResult[i+1].isdigit():
                temp.append(int(dartResult[i])*10+int(dartResult[i+1]))
                count += 1
                i += 1
            else : 
                temp.append(int(dartResult[i]))
                count += 1
        elif dartResult[i] == 'D':
            temp[count-1] = pow(temp[count-1],2)
        elif dartResult[i] == 'T':
            temp[count-1] = pow(temp[count-1],3)
        elif dartResult[i] == '*' and i==2:
            temp[count-1] *= 2
        elif dartResult[i] == '*':
            temp[count-1] *= 2
            temp[count-2] *= 2
        elif dartResult[i] == '#':
            temp[count-1] *= -1
        i += 1
    return sum(temp)