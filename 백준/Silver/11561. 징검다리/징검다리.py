import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
  n = int(input())

  start = 1
  end = n
  result = 0

  while start <= end:
    k = (start + end) // 2

    if k*(k+1)/2 <= n:
      result = max(k, result)
      start = k + 1
    else:
      end = k - 1
  
  print(result)