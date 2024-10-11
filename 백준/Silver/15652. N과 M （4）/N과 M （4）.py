import sys

input = sys.stdin.readline

def backtracking():
  if len(stack) == M:
    print(" ".join(map(str, stack)))
    return
  for i in range(1, N+1):
    if len(stack) != 0 and stack[-1] > i:
      continue
    stack.append(i)
    backtracking()
    stack.pop()

N,M = map(int, input().split())
stack = []
backtracking()