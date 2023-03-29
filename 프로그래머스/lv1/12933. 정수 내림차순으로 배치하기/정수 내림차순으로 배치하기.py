def solution(n):
    answer = 0
    temp = []
    n = str(n)
    for i in n:
        temp.append(i)
    temp.sort(reverse = True)
    temp = ''.join(s for s in temp)
    answer = int(temp)
    return answer