N, L, W, H = map(int, input().split())

start = 0
end = max(L,W,H)

for _ in range(10000):
  mid = (start + end) / 2

  count = (L // mid) * (W // mid) * (H // mid)

  if N <= count:
    start = mid
  else:
    end = mid

print("%.10f" %end)