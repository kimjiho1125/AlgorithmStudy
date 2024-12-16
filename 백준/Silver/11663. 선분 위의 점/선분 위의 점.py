import sys

input = sys.stdin.readline

# 점의 개수 N, 선분의 개수 M
N,M = map(int, input().split())
# 점의 좌표
locations = list(map(int, input().split()))
# 선분의 좌표
lines = [list(map(int, input().split())) for _ in range(M)]

locations.sort()

# 시작점과 가까운 점 찾기
def find_start(locations, target):
    start, end = 0, N - 1
    
    while start <= end:
        mid = (start + end) // 2
        if locations[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return start

def find_end(locations, target):
  start, end = 0, N-1
 
  while start <= end:
    mid = (start + end) // 2
    if locations[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  
  return start

for line in lines:
  s, e = line
  print(find_end(locations, e) - find_start(locations, s))