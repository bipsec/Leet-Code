import collections
class Solution:
    def largestGoodInteger(self, num: str) -> str:

        ans = ""
        for i in range(2, len(num)):
            temp = num[i-2:i+1]
            if num[i-2] == num[i-1] and num[i-1] == num[i] and temp > ans:
                ans = temp
        return ans


s = Solution()
print(s.largestGoodInteger("6777133339"))
print(s.largestGoodInteger("2300019"))
print(s.largestGoodInteger("42352338"))
print(s.largestGoodInteger("112"))
