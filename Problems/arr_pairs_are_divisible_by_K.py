class Solution:
    def canArrange(self, arr, k: int) -> bool:
        start, end = 0, len(arr) - 1
        flag = True

        while start < end:

            a, b = arr[start], arr[end]
            val = a + b
            print(val)
            if val % k != 0:
                flag = False
            start += 1
            end -= 1

        return flag


# wrong approach -- it's a good problem indeed!

s = Solution()
# print(s.canArrange(arr=[1, 2, 3, 4, 5, 10, 6, 7, 8, 9], k=5))
# print(s.canArrange(arr=[1, 2, 3, 4, 5, 6], k=7))
# print(s.canArrange(arr=[1, 2, 3, 4, 5, 6], k=10))
print(s.canArrange(arr=[-1, 1, -2, 2, -3, 3, -4, 4], k=3))
