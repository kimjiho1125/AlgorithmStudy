def next(w):
  # 왼쪽에 있는 수보다 오른쪽에 있는 수가 더 큰 경우를 찾음
  for i in range(len(w)-1, 0, -1):
    if w[i-1] < w[i]:
      # 오른쪽에서부터 idx보다 큰 숫자인 경우를 찾음
      for j in range(len(w)-1, i-1, -1):
        # 두 수의 위치를 바꾸고, i부터 마지막까지 원소 뒤집기
        if w[i-1] < w[j]:
          w[i-1], w[j] = w[j], w[i-1]
          return (w[:i] + (w[i:][::-1]))
  #해당되지 않는 경우 그대로 출력(마지막 순서인 경우)
  return w

#테스트 케이스 개수
n = int(input())

for _ in range(n):
  #단어 입력 받기
  word = list(input().strip())
  result = ''.join(next(word))
  print(result)