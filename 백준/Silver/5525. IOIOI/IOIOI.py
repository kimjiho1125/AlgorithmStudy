N = int(input())
M = int(input())
S = input()

answer = 0
c_idx = 0
count = 0

while c_idx < (M-1):
  if S[c_idx:c_idx+3] == 'IOI':
    c_idx += 2
    count += 1
    if count == N:
      answer += 1
      count -= 1
  else:
    c_idx += 1
    count = 0

print(answer)