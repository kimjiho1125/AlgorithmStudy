from collections import deque
import sys

n = int(input())
stack = deque()
count = 0

for _ in range(n):
    command = list(map(int,sys.stdin.readline().split()))

    if command[0] == 1:
        stack.append(command[1])
        count += 1
    elif command[0] == 2:
        if count > 0:
            print(stack.pop())
            count -= 1
        else:
            print('-1')
    elif command[0] == 3:
        print(count)
    elif command[0] == 4:
        if count == 0:
            print('1')
        else:
            print('0')
    elif command[0] == 5:
        if count > 0:
            print(stack[count-1])
        else:
            print('-1') 
