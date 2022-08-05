def fun(numbers, arr):
  cu_sum = 0
  add = arr[-1]
  start, end = arr[0]-1, arr[1]
  for i in range(start, end):
    if numbers[i] == 0:
      cu_sum += add
    else:
      cu_sum += numbers[i]
  return cu_sum


print(fun([5, 10, 10], [1, 2, 5]))
