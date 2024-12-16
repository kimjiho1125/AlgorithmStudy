import sys

input = sys.stdin.readline

n = int(input())
numbers = [input().strip() for _ in range(n)]
result = 0

for k in range(1, len(numbers[0]) + 1):
    temp = []

    for i in range(n):
        temp.append(int(numbers[i][-k:]))

    temp.sort()

    prev = -1
    check = True

    for i in range(n):
        if prev == -1:
            prev = temp[i]
        else:
            if prev == temp[i]:
                check = False
                break
            else:
              prev = temp[i]    

    # 종료조건
    if check:
        result = k
        break

print(result)    
