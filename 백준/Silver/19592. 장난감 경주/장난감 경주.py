import sys

input = sys.stdin.readline

#테스트 케이스의 수
T = int(input())

#테스트 케이스의 수만큼 반복
for _ in range(T):
  #N = 참가자의 수
  #X = 트랙의 길이
  #Y = 부스터 속도 한계치
  N, X, Y = map(int, input().rstrip().split())
  #V = 각 참가자의 속도
  V = list(map(int, input().rstrip().split()))
  best = X / max(V[:-1])
  #내가 가장 빠르다면
  if V.index(max(V)) == (N - 1):
    print(0)
  else:
    start = 0
    end = Y
    result = 0

    #start와 end 사이 이분탐색 진행
    while(start <= end):
      mid = (start + end) // 2
      #total = 도착시간
      total = (X - mid)/V[-1] + 1

      #더 빠르면 -> 최소값을 찾아야 하므로 부스터 출력 줄이기
      if total < best:
        end = mid - 1
        result = mid
      #더 느리다면 -> 부스터 출력 늘리기
      else:
        start = mid + 1

    #최대 제한 범위에 있는지 확인
    if(result != 0 and result <= Y):
      print(result)
    else:
      print(-1)