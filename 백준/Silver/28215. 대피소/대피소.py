import sys
from itertools import combinations

input = sys.stdin.readline
INF = 1e9

N, K = map(int, input().split())
#집들에 대한 정보
houses = [list(map(int, input().split())) for _ in range(N)]
#모든 가능한 대피소의 조합
combs = list(combinations(houses, K))
#최솟값을 저장할 변수
result = INF

#두 좌표의 거리를 계산하는 함수
def cal_distance(p1,p2):
  return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

#모든 집이 쉘터인 경우 예외처리
if N == K:
  print(0)

else:
  for comb in combs:
    local_max = 0
    for house in houses:
      if house not in comb:
        c_distance = INF
        #해당 집에서 가장 가까운 쉘터까지의 거리 구하기
        for s in comb:
          c_distance = min(c_distance, cal_distance(s, house))
        #가장 가까운 쉘터까지의 거리 중 가장 큰 값 찾기
        local_max = max(local_max, c_distance)
    #local_max 최소가 되는 값 찾기
    result = min(result, local_max)
  print(result)