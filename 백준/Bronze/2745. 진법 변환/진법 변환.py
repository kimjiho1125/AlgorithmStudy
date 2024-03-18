import sys
import math

n, b = sys.stdin.readline().split()
b = int(b)
n = list(n)
n.reverse()
answer = 0

for i in range(len(n)):
    if ('A' <= n[i] and 'Z' >= n[i]):
        answer += (ord(n[i]) - ord('A') + 10) * math.pow(b,i) 
    else:
        answer += int(n[i]) * math.pow(b,i)

print(int(answer))