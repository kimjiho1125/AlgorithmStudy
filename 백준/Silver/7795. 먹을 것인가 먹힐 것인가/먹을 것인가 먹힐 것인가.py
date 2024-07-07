import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):

  N,M = map(int, input().split()) 
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))

  B.sort()
  result = 0

  for target in A:
    start = 0
    end = M-1
    m_value = 0

    while start <= end:
      mid = (start + end) // 2

      if target > B[mid]:
        if m_value < mid + 1:
          m_value = mid + 1
        start = mid + 1
      else:
        end = mid - 1
    result += m_value

  print(result)