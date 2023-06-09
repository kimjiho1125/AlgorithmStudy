def solution(n, words):
    flag = False
    history = []
    lastAlpabet = ''
    for i, word in enumerate(words):
        if i == 0:
            lastAlpabet = word[-1]
            history.append(word)
        else:
            if word in history or lastAlpabet != word[0]:
                flag = True
                tempNum = (i+1) % n
                tempOrder = (i+1) // n
                number = tempNum if (tempNum != 0) else n
                order = tempOrder+1 if (tempNum != 0) else tempOrder
                return [number, order]   
            elif lastAlpabet == word[0]:
                lastAlpabet = word[-1]
                history.append(word)
                continue
            
    if flag == False:
        return [0,0]
    

