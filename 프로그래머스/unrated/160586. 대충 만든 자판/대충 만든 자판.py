def solution(keymap, targets):
    result = []
    for target in targets:
        count = 0
        Flag = True
        for s in target:
            minCount = 10000000
            for j in range(len(keymap)):
                temp = keymap[j].find(s)
                if temp < minCount and temp != -1:
                    minCount = temp + 1
            if minCount == 10000000:
                result.append(-1)
                Flag = False
                break
            else:
                count += minCount
        if Flag == False:
            continue
        else:
            result.append(count)
    return result
              
            
        
                    