import sys

n,m = map(int, sys.stdin.readline().split())

#배열 만들기
basket = []
for i in range(1,n+1):
    basket.append(i)

for i in range(m):
    i,j = map(int, sys.stdin.readline().split())
    basket[i-1:j] = list(reversed(basket[i-1:j]))

for i in range(n):
    print(basket[i], end=" ")