#정수 n
n = int(input())

#이분 탐색을 통해 입력한 수의 정수 제곱근 찾기
start = 0
end = n

while start <= end:
  mid = (start + end) // 2

  if mid ** 2 < n:
    start = mid + 1
  else:
    end = mid - 1

print(start)