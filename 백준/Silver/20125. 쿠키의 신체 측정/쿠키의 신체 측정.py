n = int(input())
board = []
heart = ()
middle = ()
answer = []

for i in range(n):
    board.append(input())

for i in range(n):
    for j in range(n):
        if board[i][j] == '*':
            heart = (i+1,j)
            break
    if len(heart):
        break

#왼쪽팔 구하기
count = 0
while True:
    if (heart[1] - 1 - count) >= 0 and board[heart[0]][heart[1] - 1 - count] == '*':
        count += 1
    else:
        answer.append(count)
        break
#오른쪽팔 구하기
count = 0
while True:
    if (heart[1] + 1 + count) < n and board[heart[0]][heart[1] + 1 + count] == '*':
        count += 1
    else:
        answer.append(count)
        break
#허리 구하기
count = 0
while True:
    if (heart[0] + 1 + count) < n and board[heart[0] + 1 + count][heart[1]] == '*':
        count += 1
    else:
        middle = (heart[0] + 1 + count, heart[1])
        answer.append(count)
        break
#왼쪽 다리 구하기
count = 0
while True:
    if (middle[0] + count) < n and board[middle[0] + count][middle[1] - 1] == '*':
        count += 1
    else:
        answer.append(count)
        break
#오른쪽 다리 구하기
count = 0
while True:
    if (middle[0] + count) < n and board[middle[0] + count][middle[1] + 1] == '*':
        count += 1
    else:
        answer.append(count)
        break

print(heart[0]+1, heart[1]+1)
print(answer[0], answer[1], answer[2], answer[3], answer[4])