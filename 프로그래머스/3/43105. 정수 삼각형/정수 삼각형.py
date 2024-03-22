def solution(triangle):
    dp = []
    #dp 배열 초기화
    for i in range(len(triangle)):
        temp = []
        for j in range(len(triangle[i])):
             temp.append(0)
        dp.append(temp)
        
    dp[0][0] = triangle[0][0]
    #계산
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i-1][0] + triangle[i][j]
            elif j == (len(triangle[i]) - 1):
                dp[i][j] = dp[i-1][len(triangle[i-1])-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1] + triangle[i][j], dp[i-1][j] + triangle[i][j])
    
    return max(dp[len(triangle)-1])