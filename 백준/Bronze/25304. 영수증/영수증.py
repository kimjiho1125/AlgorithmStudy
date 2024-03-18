import sys

x = int(sys.stdin.readline())
n = int(sys.stdin.readline())
count = 0

for i in range(n):
    a, b = map(int,sys.stdin.readline().split())
    count += (a * b)

if count == x:
    print('Yes')
else:
    print('No')