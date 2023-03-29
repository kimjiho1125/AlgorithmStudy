def solution(n):
    answer = []
    n = str(n)
    for i in reversed(range(len(n))):
        answer.append(int(n[i]))
    return answer