def solution(m, n, board):
    answer = 0
    
    #전처리 문자열 => 리스트
    for i in range(m):
        board[i] = list(board[i])
    
    while True:
        #제거될 블록들의 정보를 저장할 집합(중복을 제거하기 위해)
        removeItem = set()

        #제거할 수 있는 블록들을 조사한다
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != 0 and board[i][j] == board[i+1][j] and board[i][j] == board[i][j+1] and board[i][j+1] == board[i+1][j+1]:
                    removeItem.add((i,j))
                    removeItem.add((i+1,j))
                    removeItem.add((i,j+1))
                    removeItem.add((i+1,j+1))
                    
        #리스트로 바꾼 이유는 인덱싱을 하기 위해
        removeItems = list(removeItem)

        #종료 조건 체크
        if len(removeItems) == 0:
            break
        else:
            answer += len(removeItems)
        
        #위에서 구한 블록들을 제거한다
        for block in removeItems:
            board[block[0]][block[1]] = 0
        
        #블록들을 밑으로 땡긴다
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                zeroCount = 0
                if board[i][j] == 0:
                    zeroCount += 1
                    while (i-zeroCount >= 0 and board[i-zeroCount][j] == 0):
                        zeroCount += 1
                    if i-zeroCount >= 0:
                        board[i][j] = board[i-zeroCount][j]
                        board[i-zeroCount][j] = 0
 
    return answer