def solution(answers):
    number1 = [1,2,3,4,5] * 2000
    number2 = [2,1,2,3,2,4,2,5] * 1250
    number3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    dic = {1:0,2:0,3:0}
    result = []
    maxNum = 0 
    
    for i in range(len(answers)):
        if(answers[i] == number1[i]):
            dic[1] += 1
        if(answers[i] == number2[i]):
            dic[2] += 1
        if(answers[i] == number3[i]):
            dic[3] += 1
            
    dic = sorted(dic.items(), key=lambda x:x[1])
    
    for i in range(2,-1,-1):
        if(len(result) == 0):
            result.append(dic[i][0])
            maxNum = dic[i][1]
            continue
        elif(maxNum == dic[i][1]):
            result.append(dic[i][0])
        elif(maxNum > dic[i][1]):
            break
    result.sort()
    return result
            
        