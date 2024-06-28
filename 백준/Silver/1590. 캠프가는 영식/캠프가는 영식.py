import sys

input = sys.stdin.readline

#N = 버스의 개수
#T = 영식이가 버스 터미널에 도착하는 시간
N, T = map(int, input().split())
#모든 버스의 시작시간을 담고 있는 리스트
depart_times = []

#반복문을 통해 모든 버스의 출발시간을 depart_times에 저장
for _ in range(N):
  #S = 버스의 시작 시간
  #I = 버스의 간격
  #C = 버스의 대수
  S, I, C = map(int, input().split())
  for i in range(C):
    depart_times.append(S + I*i)

#이분 탐색을 사용하기 위해 depart_times를 오름차순으로 정렬
depart_times.sort()

#start, end 이분 탐색을 위한 변수
#w_time = 기다려야 하는 시간 => 매우 큰 수로 초기화
start = 0
end = len(depart_times)-1
w_time = 10000000000

#이분 탐색을 통해 영식이가 기다려야 하는 시간 찾기
while start <= end:
  mid = (start + end) // 2

  if 0 < depart_times[mid] - T:
     w_time = min(w_time, depart_times[mid] - T)
     end = mid - 1 
  elif 0 > depart_times[mid] - T:
    start = mid + 1
  else:
    w_time = 0
    break

#캠프에 갈 수 없는 경우 -1 출력    
if w_time == 10000000000:
  print(-1)
#캠프에 갈 수 있는 경우 기다려야 하는 시간 출력
else:
  print(w_time)     