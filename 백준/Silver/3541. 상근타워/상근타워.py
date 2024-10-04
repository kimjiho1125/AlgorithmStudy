import sys

input = sys.stdin.readline

n,m = map(int, input().split())
answer = 1e9

#n번 눌러 갈 수 있는 가장 낮은 층을 찾는 함수
def cal_min(u, d):
  start = 0
  end = n
  min_num = 1e9

  while start <= end:
    mid = (start + end) // 2
    cal = (u * mid) - (d * (n - mid))

    #음수일 경우
    if cal <= 0: 
      start = mid + 1
    #양수 -> 최솟값 찾기
    else:
      #최소값보다 작은 경우
      if cal < min_num:
        #최소값 갱신 후 더 작은 값이 있는지 탐색
        min_num = cal
        end = mid - 1
      #최소값보다 큰 경우
      else:
        #더 작은 값이 있는지 탐색
        end = end - 1

  return min_num
        
for _ in range(m):
  up, down = map(int, input().split())
  res = cal_min(up, down)
  if res < answer:
    answer = res

print(answer)