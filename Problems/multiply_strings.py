class Solution:
    def str_to_int(self, num):
        n = 0

        for item in num:
            n = 10 * n + int(item)
        return n

    def multiply(self, num1: str, num2: str) -> str:
        return str(self.str_to_int(num1) * self.str_to_int(num2))





s  =Solution()
print(s.multiply("3", "3"))
