def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    for n in A:
        for i in range(len(B)):
            if n < B[i]:
                B.pop(i)
                answer += 1
                break
                
    return answer