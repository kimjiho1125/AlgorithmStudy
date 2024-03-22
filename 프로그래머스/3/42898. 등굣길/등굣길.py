from collections import deque

def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)]   #이전 까지 경로의 개수 저장
    puddles = [[q,p] for [p,q] in puddles] #행, 열 원래대로 조정
    dp[1][1] = 1 #시작 위치
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if [i,j] in puddles:
                dp[i][j] == 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
    
    return dp[n][m]