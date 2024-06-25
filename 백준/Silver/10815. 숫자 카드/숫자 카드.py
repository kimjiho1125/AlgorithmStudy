import sys

def binary_search(array, target, start, end):
  if start > end:
    return False
  
  mid = (start + end) // 2

  if array[mid] == target:
    return True
  elif array[mid] > target:
    return binary_search(array, target, start, mid-1)
  else:
    return binary_search(array, target, mid+1, end)

input = sys.stdin.readline

#상근이가 가지고 있는 숫자 카드의 개수
n = int(input())

#숫자카드에 적혀있는 정수. 이분 탐색을 사용하기 위해 오름차순으로 정렬
n_li = sorted(list(map(int, input().rstrip().split())))

#M
m = int(input())

#M개의 정수
m_li = list(map(int, input().rstrip().split()))

#반복문을 돌며 M에 속하는 정수들을 상근이가 가지고 있는지 확인
for num in m_li:
  if binary_search(n_li, num, 0, n-1):
    print(1, end=' ')
  else:
    print(0, end=' ')