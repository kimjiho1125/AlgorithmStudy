def solution(n):
    answer = 0
    currentNum, nextNum = 0,1
    for _ in range(n):
        currentNum,nextNum = nextNum, currentNum + nextNum
    return currentNum%1234567