class Solution:
    def patrick_and_house(self):
        a, b, c = map(int, input().split())

        print(min(min(min(a + c + b, a + a + b + b), a + c + c + a), b + c + c + b))


s = Solution()
s.patrick_and_house()
