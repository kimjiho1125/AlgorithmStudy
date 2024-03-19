import sys

#각 자리수를 p번 곱해서 계산해주는 함수
def cal(num, p):
    result = 0
    for n in str(num):
        result += int(n)**p
    return result

def dfs(num):
    queue = list()
    queue.append(num)
    next_num = cal(num, p)

    while True:
        if next_num in queue:
            idx = queue.index(next_num)
            queue = queue[:idx]
            print(len(queue))
            return
        queue.append(next_num)
        next_num = cal(next_num, p)
        
a, p = map(int, sys.stdin.readline().split())

dfs(a)