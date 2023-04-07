def solution(food):
    result = '0'
    for i in range(len(food)-1,0,-1):
        if(food[i] // 2 > 0):
            for _ in range(food[i] // 2):
                result = str(i) + result + str(i)
    return result 
        