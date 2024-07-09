import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A = list(map(int, input().split()))
A.sort()

def find_GE(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

def find_G(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
    return start

def find_SE(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
    return end

for _ in range(m):
    query = list(map(int, input().split()))
    if query[0] == 1:
        ge = find_GE(A, query[1], 0, n-1)
        result = n - ge
    elif query[0] == 2:
        g = find_G(A, query[1], 0, n-1)
        result = n - g
    else:
        se = find_SE(A, query[2], 0, n-1)
        ge = find_GE(A, query[1], 0, n-1)
        result = max(0, se - ge + 1)
    print(result)