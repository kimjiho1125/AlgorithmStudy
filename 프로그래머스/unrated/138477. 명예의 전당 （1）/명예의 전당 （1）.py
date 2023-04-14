def solution(k, score):
    fame = []
    result = []
    for i in range(len(score)):
        if i+1 <= k:
            fame.append(score[i])
            fame.sort(reverse = True)
            result.append(min(fame))
        else:
            if min(fame) < score[i]:
                del fame[k-1]
                fame.append(score[i])
                fame.sort(reverse = True)
                result.append(min(fame))
            else:
                result.append(min(fame))
    return result