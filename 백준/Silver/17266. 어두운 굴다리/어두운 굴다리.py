import math

n = int(input())
m = int(input())
x = list(map(int, input().split()))

result = x[0]

#가로등이 한 개인 경우
if m == 1:
  #왼쪽까지의 거리, 오른쪽까지의 거리 중 큰 값
  result = max(x[0], n - x[0])  
else:
  for i in range(1, m):
    result = max(result, math.ceil((x[i] - x[i-1]) / 2))
result = max(result, n - x[-1])

print(result)