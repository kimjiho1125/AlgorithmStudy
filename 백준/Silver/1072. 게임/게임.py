import sys

input = sys.stdin.readline

X,Y = map(int, input().split())

start = 0
end = X
res = X
Z = (Y*100)//X
if Z >= 99:
  print(-1)
else:
  while start <= end:
    mid = (start + end) // 2
    if Z < (100*(Y+mid))//(X+mid):
      res = mid
      end = mid - 1
    else:
      start = mid + 1

  print(res)