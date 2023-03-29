def solution(x):
    x = str(x)
    sum = 0
    for i in x:
        sum += int(i)
    if(int(x) % sum == 0):
        answer = True
    else:
        answer = False
    return answer