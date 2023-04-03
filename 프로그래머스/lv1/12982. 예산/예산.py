def solution(d, budget):
    count = 0
    d.sort()
    for i in d:
        if(budget - i >= 0):
            budget -= i
            count += 1
        else:
            break
    return count