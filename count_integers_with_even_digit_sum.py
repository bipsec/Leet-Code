class Solution:
    def countEven(self, num: int) -> int:
        for i in range(1, num + 1):
            if num % i == 0:
                print(f"factor {i}", i)


s = Solution()
# print(s.countEven(4))
print(s.countEven(34))
