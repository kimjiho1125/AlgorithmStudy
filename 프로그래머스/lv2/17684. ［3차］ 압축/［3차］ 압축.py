def solution(msg):
    answer = []
    dictionary = dict()
    
    #알파벳 A~Z까지 사전 초기화
    for i in range(1,27):
        dictionary[chr(96+i).upper()] = i
        
    w,c = 0,0
    while True:
        c += 1
        if c == len(msg):
            answer.append(dictionary[msg[w:c]])
            break
        if msg[w:c+1] not in dictionary:
            dictionary[msg[w:c+1]] = len(dictionary)+1
            answer.append(dictionary[msg[w:c]])
            w=c
    
    return answer