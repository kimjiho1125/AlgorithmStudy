import sys
input = sys.stdin.readline

n, m = map(int, input().split())

basket = [i for i in range(1,n+1)]

for _ in range(m):
  idx1, idx2 = map(int, input().split())
  basket[idx1-1],basket[idx2-1] = basket[idx2-1],basket[idx1-1]

for num in basket:
  print(num, end=' ')