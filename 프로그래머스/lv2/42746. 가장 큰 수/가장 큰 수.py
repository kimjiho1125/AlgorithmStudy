def solution(numbers):
    numbers = list(map(str,numbers))
    result = list()
    for i in range(len(numbers)):
        temp = numbers[i]
        while len(temp) < 4:
            temp += temp
        result.append([temp, numbers[i]])
    result.sort(reverse = True)
    answer = str(int("".join(r[1] for r in result)))       
    
    return answer