def solution(s):
    x = '';
    xCount = 0
    theOtherCount = 0
    result = 0
    
    for i in s:
        if x == '':
            x = i
            xCount = 1
            continue
            
        if x != i:
            theOtherCount += 1
        else:
            xCount += 1
            
        if xCount == theOtherCount:
            result += 1
            x = '';
            xCount = 0
            theOtherCount = 0
    if x:
        result += 1
        
    return result
       