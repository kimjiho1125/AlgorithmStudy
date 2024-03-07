from collections import Counter

def solution(cards):
    answer = []
    
    for i in range(len(cards)):
        tmp = 0
        while cards[i]:
            nextIdx = cards[i] - 1
            cards[i] = 0
            i = nextIdx
            tmp += 1
        answer.append(tmp)
        
    answer.sort()
    
    return answer[-1] * answer[-2]