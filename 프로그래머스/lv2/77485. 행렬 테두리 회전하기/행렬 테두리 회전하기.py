def solution(rows, columns, queries):
    answer = []
    
    #행렬 초기화
    table = [[0 for j in range(columns)] for i in range(rows)]
    
    for i in range(rows):
        for j in range(columns):
            table[i][j] = (i) * columns + j + 1
    
    for query in queries:
        #초기화
        i = query[0]-1
        j = query[1]-1
        minI = query[0]-1
        minJ = query[1]-1
        maxI = query[2]-1
        maxJ = query[3]-1
        mValue = table[i][j]
        temp = 0
        
        #오른쪽으로 쭉 변경
        while j < maxJ:
            if temp != 0 and temp < mValue:
                mValue = temp
            if temp == 0:
                temp = table[i][j+1]
                table[i][j+1] = table[i][j]
                j += 1
            elif temp != 0:
                temp, table[i][j+1] = table[i][j+1], temp
                j += 1
            
        #아래쪽으로 쭉 변경
        while i < maxI:
            if temp < mValue:
                mValue = temp
            temp, table[i+1][j] = table[i+1][j], temp
            i += 1
        #왼쪽으로 쭉 변경
        while j > minJ:
            if temp < mValue:
                mValue = temp
            temp, table[i][j-1] = table[i][j-1], temp
            j -= 1
        #위쪽으로 쭉 변경
        while i > minI:
            if temp < mValue:
                mValue = temp
            temp, table[i-1][j] = table[i-1][j], temp
            i -= 1
        
        #작업이 끝나면 mValue 값을 answer에 넣는다
        answer.append(mValue)
        
    return answer