def solution(n):
    result = []
    #배열 초기화
    field = [[0 for i in range(n)] for j in range(n)]
    r,c = 0,0
    field[r][c] = 1
    
    currentNum = 1
    #등차수열 합공식
    finalNum = n*(n+1) / 2
    
    #종료 조건 - currentNum가 finalNum와 같아질 때
    while currentNum < finalNum:
        
        while r+1 <= n-1 and field[r+1][c] == 0:
            currentNum += 1
            r,c = r+1,c
            field[r][c] = currentNum
        
        while c+1 <= n-1 and field[r][c+1] == 0:
            currentNum += 1
            r,c = r,c+1
            field[r][c] = currentNum
        
        while c-1 >= 0 and r-1 >= 0 and field[r-1][c-1] == 0:
            currentNum += 1
            r,c = r-1, c-1
            field[r][c] = currentNum
            
    #0을 제거하고 최종 결과 리스트로 만들기
    for i in range(n):
        for j in range(n):
            if field[i][j] != 0:
                result.append(field[i][j])
        
            
    return result