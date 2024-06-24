def binary_search(array, target, start, end):
  if start > end or array[0] > target or array[49] < target:
    return 0
  
  mid = (start + end) // 2

  if array[mid] > target:
    print(array[mid], end=' ')
    return binary_search(array, target, start, mid-1)
  elif array[mid] < target:
    print(array[mid], end=' ')
    return binary_search(array, target, mid+1, end)
  else:
    print(array[mid], end=' ')


array = [i for i in range(1,51)]
while True:
  target = int(input())
  result = binary_search(array, target, 0, 49)
  if result == 0:
    break
  print(sep = '\n')