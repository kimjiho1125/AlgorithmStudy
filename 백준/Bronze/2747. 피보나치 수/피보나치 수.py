import sys

def solution():

    n = int(sys.stdin.readline())

    a = 0
    b = 1
    if n==0:
        print(0)
        return
    if n==1:
        print(1)
        return 
           
    for _ in range(n-1):
        c = a + b
        a, b = b, c

    print(c)

solution()