import sys

while True:
  #상근이가 가지고 있는 CD의 수(N)와 선영이가 가지고 있는 CD의 수(M) 입력
  n, m = map(int, sys.stdin.readline().split())
  #n과 m이 모두 0일 경우 종료
  if n == 0 and m == 0:
    break

  result = 0
  dic = {}
  #상근이가 가지고 있는 CD의 번호를 오름차순으로 입력받으며 딕셔너리에 저장
  for _ in range(n):
    cd = int(sys.stdin.readline())
    dic[cd] = 1
  #선영이가 가지고 있는 CD의 번호를 오름차순으로 입력받으며 딕셔너리에 해당 번호가 있는지 확인
  for _ in range(m):
    cd = int(sys.stdin.readline())
    if cd in dic:
      result += 1
  
  print(result)