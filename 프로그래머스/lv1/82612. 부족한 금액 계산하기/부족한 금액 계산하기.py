def solution(price, money, count):
    cost = 0
    for i in range(1,count+1):
        cost += price*i
    if(money - cost < 0):
        return abs(money-cost)
    return 0