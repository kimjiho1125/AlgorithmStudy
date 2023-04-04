def solution(s):
    numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
    intNumbers = ['0','1','2','3','4','5','6','7','8','9']
    for i in range(len(numbers)):
        if(s.find(numbers[i]) >= 0):
            s = s.replace(numbers[i],intNumbers[i])
    return int(s)
        