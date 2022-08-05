def increament(num, inc):
  for i in range(len(num) - 1, -1, -1):
    carry = 0
    val = num[-1] + inc
    print(val)
    if val >= 10:
      carry = val - carry
    elif val < 10:
      carry = val
    num[i] = carry

  print(num)


print(increament([1, 2, 3], 2))
