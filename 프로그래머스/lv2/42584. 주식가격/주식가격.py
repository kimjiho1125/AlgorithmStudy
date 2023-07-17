from collections import deque

def solution(prices):
    answer = []
    dq = deque(prices)
    while(dq):
        price = dq.popleft()
        count = 0
        for com_price in dq:
            count += 1
            if price > com_price:
                break
        answer.append(count)
    return answer