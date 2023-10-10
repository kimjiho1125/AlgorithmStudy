def solution(board):
    #DP를 사용하지 않았을 경우에는 3중 for문을 사용해야 함. 행과 열의 최대 크기가 1000이므로 최대 1,000,000,000번 연산한다
    #파이썬은 1초에 약 2천만번 연산 가능하므로 약 50초가 걸린다. (통상적인 알고리즘 문제는 2~3초 안에 해결해야함)
    #따라서 DP를 이용하여 문제를 풀어야 한다.
    #핵심은 현재 위치에서 가능한 최대 크기의 정사각형 한 변의 길이를 찾는 것
    
    #사용할 변수들 초기화
    row = len(board)
    column = len(board[0])
    answer = 0
    DP = [[0] * column for _ in range(row)]
    DP[0] = board[0]
    
    #DP배열 초기화
    for i in range(1,row):
        DP[i][0] = board[i][0]

        
    #2중 for문으로 가능한 최대 크기의 정사각형의 한 변의 길이 구하기
    for i in range(1,row):
        for j in range(1,column):
            if board[i][j] == 1:
                DP[i][j] = min(DP[i][j-1],DP[i-1][j],DP[i-1][j-1]) + 1
    
    #한 변의 길이의 최대값 구하기
    for i in range(row):
        temp = max(DP[i])
        answer = max(answer,temp)
    
    #넓이 리턴
    return answer**2
      
   