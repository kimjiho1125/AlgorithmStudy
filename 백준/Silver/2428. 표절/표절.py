import sys

input = sys.stdin.readline

N = int(input())
s_file = list(map(int, input().split()))
s_file.sort()
cnt = 0

for i in range(N):
  start = i
  end = N-1

  while start <= end:
    mid = (start + end) // 2

    if s_file[i] >= 0.9 * s_file[mid]:
      start = mid + 1
    else:
      end = mid - 1
  
  cnt += start - i - 1

print(cnt)