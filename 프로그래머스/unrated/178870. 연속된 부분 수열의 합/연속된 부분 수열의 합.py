def solution(sequence, k):
    answer = []
    sub_sum = 0
    l = 0
    r = -1
    
    while True:
        if sub_sum < k:
            r += 1
            if r >= len(sequence):
                break
            sub_sum += sequence[r]
        else: 
            sub_sum -= sequence[l]
            if l >= len(sequence):
                break
            l += 1
        if sub_sum == k:
            answer.append([l,r])
    
    answer.sort(key=lambda x: (x[1]-x[0], x[0]))
    return answer[0]