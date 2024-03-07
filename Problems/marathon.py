import sys

Iarr = lambda: list(map(int, input().split()))

# Take input array
def takeiar():
    return list(map(int, sys.stdin.readline().rstrip("\r\n").split()))


def marathon():
    n = int(input())
    for i in range(n):
        nums = Iarr()
        # print(nums)

        count = 0
        for j in range(1, len(nums)):
            if nums[0] < nums[j]:
                count += 1
        print(count)


marathon()
# print(marathon([2, 3, 4, 1]))
# print(marathon([10000, 0, 1, 2]))
# print(marathon([500, 600, 400, 300]))
# print(marathon([0, 9999, 10000, 9998]))
