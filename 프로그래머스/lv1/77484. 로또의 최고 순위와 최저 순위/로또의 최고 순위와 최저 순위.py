def Rank(num):
    if num == 6:
        return 1
    elif num == 5:
        return 2
    elif num == 4:
        return 3
    elif num == 3:
        return 4
    elif num == 2:
        return 5
    else:
        return 6
            
def solution(lottos, win_nums):
    extraCount = 0
    count = 0
    answer = []
    for lotto in lottos:
        if lotto in win_nums:
            count += 1
        elif lotto == 0:
            extraCount += 1
    answer.append(Rank(count + extraCount))
    answer.append(Rank(count))
    return answer
    
    
    
            