def solution(order):
    answer = 0
    currentNum = 1
    assist = []
    for num in order:
        while True:
            if currentNum < num:
                assist.append(currentNum)
                currentNum += 1
            elif currentNum == num:
                answer += 1
                currentNum += 1
                break
            elif currentNum > num:
                if assist.pop() == num:
                    answer += 1
                    break
                else:
                    return answer
    return answer