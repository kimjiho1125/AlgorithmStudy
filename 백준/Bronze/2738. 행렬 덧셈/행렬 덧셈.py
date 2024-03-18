import sys

n,m = map(int,sys.stdin.readline().split())

A = list()
B = list()
result = list()

for _ in range(n):
    A.append(list(map(int,sys.stdin.readline().split())))
for _ in range(n):
    B.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    result.append(list(map(lambda x,y: x+y, A[i] , B[i])))

#출력
for x in result:
    for num in x:
        print(num, end=" ")
    print(end="\n")