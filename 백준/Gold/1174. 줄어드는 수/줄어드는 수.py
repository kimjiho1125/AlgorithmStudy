import sys

input = sys.stdin.readline

def backtracking():
  if number:
    result.add(int("".join(map(str, number))))
  for i in range(10):
    if not number or number[-1] > i:
      number.append(i)
      backtracking()
      number.pop()

N = int(input().rstrip())
result = set()
number = []

backtracking()
result = sorted(result)
print(result[N-1] if len(result) >= N else -1)