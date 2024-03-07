def digits():
  nums = int(input())
  num = list(str(nums))
  result = []
  res = ""

  for i in range(len(num)):
    val = num[i]
    for j in range(0, len(num)):
      res += str(val)
      if len(res) == len(num):
        result.append(int(res))
        res = ""
  result.append(nums)
  result.sort()
  print(result)
  index = 0
  for item in range(len(result)):
    if result[item] > nums:
      return result[item+1]
    elif result[item] > nums:
      return result[item]


print(digits())