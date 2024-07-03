import sys

input = sys.stdin.readline

N = int(input())
w, h = map(int, input().split())

coord = set(tuple(map(int, input().split())) for _ in range(N))

cnt = 0

for x,y in coord:
  if((x+w,y) in coord) and ((x,y+h) in coord) and ((x+w, y+h) in coord):
    cnt += 1 

print(cnt)