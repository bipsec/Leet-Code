from collections import Counter


class Solution:
    def canArrange(self, arr, k: int) -> bool:

        remainder_count = Counter((x % k + k) % k for x in arr)

        for rem in list(remainder_count.keys()):
            if rem == 0:
                if remainder_count[rem] % 2 != 0:
                    return False
            else:
                if remainder_count[rem] != remainder_count[k - rem]:
                    return False

        return True


# wrong approach -- it's a good problem indeed!
# remainder niye vaba uchit chilo!
# not mine

s = Solution()
# print(s.canArrange(arr=[1, 2, 3, 4, 5, 10, 6, 7, 8, 9], k=5))
# print(s.canArrange(arr=[1, 2, 3, 4, 5, 6], k=7))
# print(s.canArrange(arr=[1, 2, 3, 4, 5, 6], k=10))
print(s.canArrange(arr=[-1, 1, -2, 2, -3, 3, -4, 4], k=3))
print(s.canArrange(arr=[3, 8, 7, 2], k=10))
print(s.canArrange(arr=[1, 2], k=3))
