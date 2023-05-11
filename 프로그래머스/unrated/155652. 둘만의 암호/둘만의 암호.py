def solution(s, skip, index):
    result = []
    skip = list(skip)
                              
    for k in s:    
        temp = []
        firstIndex = ord(k)
        LastIndex = firstIndex + index
        i = firstIndex + 1
        count = 0
        while count != index:
            if i >= 97 and i <= 122 and chr(i) not in skip:
                temp.append(chr(i))
                count += 1
            elif i > 122 and chr(97 + i%123) not in skip:
                i = 97 + i%123
                temp.append(chr(i))
                count += 1
            i += 1
        
        result.append(temp[index-1])
        answer = ''.join(result)
    
    return answer