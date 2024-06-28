import sys

input = sys.stdin.readline

#테스트 케이스의 수
T = int(input())

#이분 탐색
def binary_search(array, target, start, end):
  if start > end:
    return False
  
  mid = (start + end) // 2

  if array[mid] < target:
    return binary_search(array, target, mid + 1, end)
  elif array[mid] > target:
    return binary_search(array, target, start, mid - 1)
  else:
    return True

for _ in range(T):
  #수첩 1에 적어놓은 정수의 개수와 수첩 1에 적힌 숫자들
  N = int(input())
  note1 = list(map(int,input().split()))
  #수첩 2에 적어놓은 정수의 개수와 수첩 2에 적힌 숫자들
  M = int(input())
  note2 = list(map(int,input().split()))

  #이분 탐색을 사용하기 위해 수첩1을 정렬
  note1.sort()

  #이분 탐색으로 결과 찾기
  for num in note2:
    if binary_search(note1, num, 0, N-1):
      print(1)
    else:
      print(0)