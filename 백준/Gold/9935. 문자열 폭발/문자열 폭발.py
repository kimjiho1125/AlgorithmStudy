string = input()
bomb_string = list(input())

n = len(bomb_string)
stack = []

for c in string:
  stack.append(c)
  if stack[-n:] == bomb_string:
    for _ in range(n):
      stack.pop()

print(''.join(stack) if stack else "FRULA")