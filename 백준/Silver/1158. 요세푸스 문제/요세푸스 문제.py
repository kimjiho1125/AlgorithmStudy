n,k = map(int, input().split())
queue = []
result = []
idx = 0

for i in range(n):
  queue.append(i+1)

while queue:
    idx += k - 1
    if idx >= len(queue):
        idx %= len(queue)
    result.append(str(queue.pop(idx)))

print("<" + ", ".join(result) + ">")