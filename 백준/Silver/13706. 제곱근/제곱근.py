N = int(input())

start = 0
end = N
result = 0

while start <= end:
  mid = (start + end) // 2
  
  num = pow(mid,2)

  if N < num:
    end = mid-1
  elif N > num:
    start = mid+1
  else:
    result = mid
    break

print(result)