def solution(topping):
    answer = 0
    olderBro = {}
    youngerBro = {}
    for item in topping:
        if item not in olderBro:
            olderBro[item] = 1
        else:
            olderBro[item] += 1
    
    for item in topping:
        if item not in youngerBro:
            youngerBro[item] = 1
            olderBro[item] -= 1
        else:
            youngerBro[item] += 1
            olderBro[item] -= 1
            
        if youngerBro[item] == 0:
            del youngerBro[item]
        if olderBro[item] == 0:
            del olderBro[item]
            
        if len(olderBro.keys()) == len(youngerBro.keys()):
            answer += 1
    return answer