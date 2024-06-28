import sys

input = sys.stdin.readline

#이분 탐색
def binary_search(array, target, start, end):
  if start > end:
    return -1
  
  mid = (start + end) // 2

  if array[mid] < target:
    return binary_search(array, target, mid + 1, end)
  elif array[mid] > target:
    return binary_search(array, target, start, mid - 1)
  else:
    
    return binary_search(array, target, start, mid - 1)

#N = 리스트 A의 원소의 개수
#M = 질문의 개수
N, M = map(int, input().split())
A = []
Q = []

#리스트 A 입력 받기
for _ in range(N):
  A.append(int(input()))
#질문에 해당하는 정수 D 입력받기
for _ in range(M):
  Q.append(int(input()))

#A를 오름차순으로 정렬한 배열 B
B = sorted(A)

#이분 탐색을 통해 탐색 진행
for target in Q:
  start = 0
  end = N-1
  idx = -1
  while start <= end:
    mid = (start + end) // 2
    if B[mid] < target:
      start = mid +1
    elif B[mid] > target:
      end = mid - 1
    else:
      idx = mid
      end = mid - 1
  if idx == -1:
    print(-1)
  else:
    print(idx)