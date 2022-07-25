import itertools

def iteration(nums):
  result = []
  for i in range(1, len(nums) + 1):
    result.extend(list(itertools.permutations(nums, r=i)))
  res = result[-1]

  for value in res:
    print(value, end=" ")
  print("")

def permutaions():
  n = int(input())
  for j in range(n):
    val = int(input())
    dupes = []
    result = []
    for i in range(1, val + 1):
      dupes.append(i)

    iteration(dupes)


permutaions()


