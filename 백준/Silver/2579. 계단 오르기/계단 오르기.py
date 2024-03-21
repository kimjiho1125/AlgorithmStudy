n = int(input())
stairs = [int(input()) for _ in range(n)]
dp = stairs[:1] + [0] * (n) 


for i in range(1,n):
    dp[i] = max(stairs[i] + stairs[i-1] + dp[i-3], stairs[i] + dp[i-2])

print(dp[n-1])
