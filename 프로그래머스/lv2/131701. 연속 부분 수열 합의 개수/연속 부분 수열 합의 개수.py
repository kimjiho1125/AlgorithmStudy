def solution(elements):
    result = []
    maxlen = len(elements)
    for i in range(1,maxlen+1):
        for k in range(maxlen):
            if k+i <= maxlen:
                temp = elements[k:k+i]
            elif k+i > maxlen:
                temp = elements[k:maxlen+1] + elements[0:(k+i)-maxlen]
            result.append(sum(temp))
    result = set(result)
 
    return len(result)