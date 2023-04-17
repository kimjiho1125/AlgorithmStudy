def solution(name, yearning, photo):
    result = []
    for one in photo:
        answer = 0
        for item in one:
            if item in name:
                answer += yearning[name.index(item)]  
        result.append(answer)
    return result                           